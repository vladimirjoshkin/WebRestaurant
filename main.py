from flask import Flask, request, render_template, redirect
import sqlite3
import os

app = Flask(__name__)

I18N_DATABASE_PATH = os.path.join("databases", "i18n.db")


@app.route("/")
@app.route("/index")
def hello():
    return render_template("index.html")


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