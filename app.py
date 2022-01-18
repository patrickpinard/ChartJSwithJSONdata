# Auteur  : Patrick Pinard 
# Date    : 17.1. 2022
# Objet   : Graph avec ChartJS et data au format JSON
# Version : 1.0  

# -*- coding: utf-8 -*-

#   Clavier MAC :      
#  {} = "alt/option" + "(" ou ")"
#  [] = "alt/option" + "5" ou "6"
#   ~  = "alt/option" + n    
#   \  = Alt + Maj + / 
# 

from flask import Flask, render_template, request, jsonify
import datetime, os, json

# Création de l'APPLICATION FLASK:
app = Flask(__name__)


def LoadJSONData():
    '''
    chargement de l'ensemble des données dans un template JSON   
    '''

    jsonfile = {
            "jsonarray": [{
                "date": "17.1.2022",
                "temp": 12
            }, {
                "date": "18.1.2022",
                "temp": 14
            },
            {
                "date": "19.1.2022",
                "temp": 16
            },
            {
                "date": "20.1.2022",
                "temp": 18
            },
            {
                "date": "21.1.2022",
                "temp": 10
            },
            {
                "date": "22.1.2022",
                "temp": 6
            }]
        }

    return jsonfile


@app.route("/", methods=['GET'])
def index():
    '''
    chargement de la page principale index.html avec données dans template. 
    '''

    return render_template('index.html', jsonfile = jsonify(LoadJSONData())) 
    

@app.route("/getJSONdata", methods=['GET'])
def getJSONdata():
    '''
    chargement des données au format JSON. 
    '''
    
    return render_template('index.html', jsonfile = jsonify(LoadJSONData()))

if __name__ == '__main__': 
    
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port = 80, debug=True)        
    
    
  
    
    



    

    
   





