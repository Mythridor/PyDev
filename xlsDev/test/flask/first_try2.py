#! /usr/local/bin/python3.6

import os
import sqlite3
import time
from functools import wraps

from flask import Flask, render_template, request, redirect, Response

app = Flask(__name__)


@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(500)
def ma_page_erreur(error):
    return render_template('error.html', codeError=error.code)

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'test'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        print(auth)
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


def db_connection(name):
    conn = sqlite3.connect(name)
    return conn.cursor(), conn


def request_executor(db_name, requete):
    cursor, conn = db_connection(db_name)
    cursor.execute(requete)
    db_end_transaction(conn)


def db_end_transaction(conn):
    conn.commit()
    conn.close()


def db_init():
    start_time = time.time()
    print(" * [LOGGER] >>> Checking database...")
    request_executor('ma_base.db', """DROP TABLE 'users'""")
    request_executor('ma_base.db', """
    CREATE TABLE IF NOT EXISTS users(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         identifiant TEXT,
         fonction TEXT)
         """)
    users = list()
    users.append(("Tintin", "Humain"))
    users.append(("Milou", "Chien"))
    cursor, conn = db_connection('ma_base.db')
    cursor.executemany("""
    INSERT INTO users(identifiant, fonction) VALUES(?, ?)""", users)
    db_end_transaction(conn)
    print(" * [LOGGER] >>> Database checked in " + "{:.3f}".format(time.time() - start_time) + "s...")


@app.route("/generate_fiche")
def evalFicheGenerator():
    os.system("python3.6 fiche_eval_generator.py")
    return redirect("/dashboard")

@app.route("/")
@requires_auth
def hello():
    conn = sqlite3.connect('ma_base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return render_template("boot.html", value=rows)

if __name__ == '__main__':
    db_init()
    app.run(debug=True)
