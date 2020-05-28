import os
import sqlite3

import reservation
from table import Table
from reservation import Reservation


BOOKING_DATABASE_PATH = os.path.join("databases", "booking.db")


def get_booking_list():
    booking_list = []
    # getting products
    conn = sqlite3.connect(BOOKING_DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tables")
    for table_sql_tpl in cur.fetchall():
        booking_list.append(get_table(table_sql_tpl[0]))
    print(booking_list)
    conn.close()
    return booking_list


def get_table(table_id):
    conn = sqlite3.connect(BOOKING_DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tables WHERE id = ?", (table_id,))
    table_sql_tpl = cur.fetchone()
    ctable = Table()
    ctable.id = table_id
    ctable.name = table_sql_tpl[1]
    ctable.description = table_sql_tpl[2]
    ctable.image_filename = table_sql_tpl[3]
    ctable.available_from = str_to_array_time(table_sql_tpl[4])
    ctable.available_to = str_to_array_time(table_sql_tpl[5])
    ctable.reservations = get_reservations(table_id)
    conn.close()
    return ctable

def str_to_array_time(string_time):
    hour = string_time.split(":")[0]
    minute = string_time.split(":")[1]
    return [hour, minute]

def str_to_array_date(string_date):
    year = string_date.split(".")[0]
    month = string_date.split(".")[1]
    day = string_date.split(".")[2]
    return [year, month, day]

def get_reservations(table_id):
    resevations = []
    conn = sqlite3.connect(BOOKING_DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM reservation WHERE table_ref = ?", (table_id,))
    for reservation_sql_tpl in cur.fetchall():
        reservation = Reservation()
        reservation.id = reservation_sql_tpl[0]
        reservation.table_id = reservation_sql_tpl[1]
        reservation.date = str_to_array_date(reservation_sql_tpl[2])
        reservation._from = str_to_array_time(reservation_sql_tpl[3])
        reservation._to = str_to_array_time(reservation_sql_tpl[4])
        resevations.append(reservation)
    conn.close()
    return resevations