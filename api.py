#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, jsonify, request, send_from_directory
import json, sqlite3, hashlib

app = Flask(__name__)

conn = sqlite3.connect('Prepget.db')
c = conn.cursor()


@app.route("/", methods=['GET'])
def index():
    c.execute("SELECT Nom FROM Paquets")
    resultquery = c.fetchall()
    name = "["
    for result in resultquery:
        name += str(result) + ", "
    name = name[:-2] + "]"
    return name

@app.route("/packet/<path:Paquet>")

def dl_paquet(Paquet):

    c.execute("SELECT Nom FROM Paquets WHERE Nom = '"+Paquet+"'")
    resultquery = c.fetchall()
    if len(resultquery) == 1:
        c.execute("SELECT Path FROM Paquets WHERE Nom = '"+Paquet+"'")
        resultquery = c.fetchall()
        return(resultquery[0])
    else:
        c.execute("SELECT Logiciel FROM Paquets WHERE Logiciel = '"+Paquet+"'")
        resultquery = c.fetchall()

        if len(resultquery) >= 1:
            c.execute("SELECT Path FROM Paquets WHERE Logiciel = '"+Paquet+"' ORDER BY Version DESC")
            resultquery = c.fetchall()
            return (resultquery[0])
        elif len(resultquery) == 0:
            c.execute("SELECT Path FROM Paquets WHERE Nom LIKE '"+Paquet+"%' ORDER BY Version DESC")
            resultquery = c.fetchall()
            if len(resultquery) >= 1:
                return (resultquery[0])
            else:
                return "Ce paquet n'existe pas"

# @app.route("/LOGIN/<string:Username>/<string:Password>")

def register():
    
    resultquery = c.execute("SELECT Username FROM User WHERE Username ='"+Username+"'")
    resultquery = c.fetchall()
    if len(resultatquery) > 0:
        resultquery = c.execute("SELECT Username FROM User WHERE Password ='"+Password+"' ANDUsername ='"+Username+"'")
        resultquery = c.fetchall()
        if resultquery > 0:
            print "vous etes connecté"
        else:#3 essais ?
            print "mauvais mot de passe"

@app.route("/REGISTER/<string:Username>/<string:Password>")
def register():
    resultquery = c.execute("SELECT Username FROM User WHERE Username ='"+Username+"'")
    resultquery = c.fetchall()
    if len(resultatquery) == 0:
        c.execute("INSERT INTO USER (Username) VALUES ('"+Username+"')")
        c.execute("INSERT INTO USER (Password) VALUES ('"+Password+"')")
        print "Vous etes inscrit et connecté"
    else:
        print "ce pseudo existe deja"




app.run(host='0.0.0.0', port=8080)
