#! /usr/local/bin/python3.6

import sqlite3
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


def db_populate():
    users = list()
    conn = sqlite3.connect('ma_base.db')
    cursor = conn.cursor()
    users.append(("Benjamin ENOU", "Développeur"))
    users.append(("Julien FAVRE", "Chef de projet"))
    cursor.executemany("""
    INSERT INTO users(identifiant, fonction) VALUES(?, ?)""", users)
    conn.commit()
    conn.close()


def db_init():
    conn = sqlite3.connect('ma_base.db')
    cursor = conn.cursor()
    print(" * LOGGER >>> Checking Database...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         identifiant TEXT,
         fonction TEXT)
         """)
    conn.commit()
    conn.close()
    db_populate()


@app.route("/generate_fiche")
def evalFicheGenerator():
    os.system("python3.6 fiche_eval_generator.py")
    return redirect("/dashboard")


@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(500)
def ma_page_erreur(error):
    return render_template('error.html', codeError=error.code)


@app.route("/")
def hello():
    return render_template('accueil.html')


@app.route("/download")
def download():
    mail = request.args['mail']
    password = request.args['password']

    if mail == "test@test.test" and password == "test":
        return redirect('/dashboard')
    else:
        return "Authentication failed!"


@app.route("/dashboard")
def success():
    result = "<!DOCTYPE html><html>" \
             "<head></head>" \
             "<body>" \
             "<h1 style='text-align: center;'>Veuillez sélectionner le collaborateur dont vous souhaitez faire l'évaluation</h1>" \
             "<div style='width: 17%; margin: auto; border: 2px solid black; border-radius: 5px; padding: 15px;'><form action='/test'><select name='role'>"
    conn = sqlite3.connect('ma_base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        result += "<option value='" + row[2] + "'>{0} : {1} - {2}</option>".format(row[0], row[1], row[2])

    result += "</select><br /><input style='margin: auto;' type='submit' value='Sélectionner' /></form></div><a href='/generate_fiche'>Génération de fiches</a></body></html>"
    conn.close()
    return result.encode('utf-8')


if __name__ == '__main__':
    db_init()
    app.run(debug=True)
