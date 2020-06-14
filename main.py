from flask import Flask, request, render_template, redirect, make_response
import sqlite3
import os
from menu import get_product_list
from booking import get_booking_list, get_table
from table import Table
from datetime import datetime

app = Flask(__name__)

I18N_DATABASE_PATH = os.path.join("databases", "i18n.db")


@app.route("/")
@app.route("/index")
def hello():
    return render_template("index.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/about-us")
def about_us():
    return render_template("about-us.html")


@app.route("/booking")
def booking():
    booking_list = get_booking_list()
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    date = [year, month, day]
    print(date)
    return render_template("booking.html", booking_list=booking_list, date=date)


@app.route("/menu", methods=['GET'])
def menu():
    lang = request.args.get('lang', default='ru', type=str)
    product_list = get_product_list(lang)
    client_id = request.cookies.get('client_id')
    response = make_response(render_template("menu.html", product_list=product_list))
    if not len(client_id) > 0:
        response.set_cookie('client_id', str(datetime.now()))
    return response

@app.route("/card", methods=['GET'])
def card():
    lang = request.args.get('lang', default='ru', type=str)
    product_list = get_product_list(lang)
    client_id = request.cookies.get('client_id')
    added_product_ids_str = request.cookies.get('added_products')
    added_product_ids_str = added_product_ids_str.split(',')
    #print(added_product_ids_str)
    added_product_ids = []
    for id_str in added_product_ids_str:
        added_product_ids.append(int(id_str))
    response = make_response(render_template("card.html", product_list=product_list, added_product_ids=added_product_ids))
    if not len(client_id) > 0:
        response.set_cookie('client_id', str(datetime.now()))
    return response

def check_table_availiability(table, date, fromHour, toHour):
    availability = []
    for reservation in table.reservations:
        if (reservation.same_date(date)):
            if (toHour < reservation.get_from_hour()) or (fromHour > reservation.get_to_hour()):
                availability.append(True)
            else:
                availability.append(False)
    if len(availability) == 0:
        return True
    for av in availability:
        if not av:
            return False
    return True


@app.route("/reserveTable", methods=['POST'])
def reserve_table():
    BOOKING_DATABASE_PATH = os.path.join("databases", "booking.db")
    tableId = request.args.get('tableId', type=int)
    date = str(request.args.get('date', type=str))
    date = [date.split('-')[0], date.split('-')[1], date.split('-')[2]]
    date = date[0] + "." + date[1] + "." + date[2]
    fromHour = request.args.get('fromHour', type=int)
    if(fromHour < 10):
        fromHour = "0" + fromHour
    fromMinute = request.args.get('fromMinute', type=int, default=0)
    toHour = request.args.get('toHour', type=int)
    if(toHour < 10):
        toHour = "0" + toHour
    toMinute = request.args.get('toMinute', type=int, default=0)
    table = get_table(tableId)
    if(check_table_availiability(table=table, date=date, fromHour=fromHour, toHour=toHour)):
        conn = sqlite3.connect(BOOKING_DATABASE_PATH)
        cur = conn.cursor()
        cur.execute("INSERT INTO reservation (table_ref, date, _from, _to) VALUES (?, ?, ?, ?)", (tableId, date, str(fromHour) + ":00", str(toHour) + ":00"))
        conn.commit()
        cur.execute("SELECT * FROM reservation WHERE table_ref=? AND date=? AND _from=? AND _to=?", (tableId, date, str(fromHour) + ":00", str(toHour) + ":00"))
        reservation_data = cur.fetchone()
        text = "Бронирование стола № " + str(reservation_data[1]) + " " + str(reservation_data[2]) + " c " + str(reservation_data[3]) + " по " + str(reservation_data[4]) + " создано.\nНомер бронирования " + str(reservation_data[0]) + "."
        conn.close()
        return text
    else:
        return "Бронировния на выбранное вами время недоступно. Выберете другое время и (или) дату."

@app.route("/checkReservationAvailable", methods=['GET'])
def checkReservationAvailable():
    tableId = request.args.get('tableId', type=int)
    date = str(request.args.get('date', type=str))
    date = [date.split('-')[0], date.split('-')[1], date.split('-')[2]]
    fromHour = request.args.get('fromHour', type=int)
    fromMinute = request.args.get('fromMinute', type=int)
    toHour = request.args.get('toHour', type=int)
    toMinute = request.args.get('toMinute', type=int)
    table = get_table(tableId)
    print(table)
    #if len(table.reservations) == 0:
    #    return "True"
    '''
    availability = []
    for reservation in table.reservations:
        if(reservation.same_date(date)):
            if (toHour < reservation.get_from_hour()) or (fromHour > reservation.get_to_hour()):
                availability.append(True)
            else:
                availability.append(False)
    if len(availability) == 0:
        return "True"
    for av in availability:
        if not av:
            return "False"
    return "True"
    '''
    if(check_table_availiability(table=table, date=date, fromHour=fromHour, toHour=toHour)):
        return "True"
    else:
        return "False"


@app.context_processor
def translation_processor():
    def get_translated_string(key_str, lang="ru"):
        conn = sqlite3.connect(I18N_DATABASE_PATH)
        cur = conn.cursor()
        key_str_id = cur.execute("SELECT id FROM key_strings WHERE key_str = \'?\'", (key_str,)).fetchone()[0]
        translated_string = cur.execute("SELECT str FROM translations WHERE key_str_id = \'?\' AND lang = \'?\'", (key_str_id, lang)).fetchone()[0]
        conn.close()
        return translated_string
    return dict(get_translated_string=get_translated_string)