from flask_mysqldb import MySQL
from datetime import date
import json

def datenow():
    today = date.today()
    return today

def connection(app):
    f = open('config/config.json')
    config = json.load(f)
    
    app.config['MYSQL_HOST'] = config['system_localhost']
    app.config['MYSQL_USER'] = config['system_username']
    app.config['MYSQL_PASSWORD'] = config['system_password']
    app.config['MYSQL_DB'] = config['system_database']
    
    mysql = MySQL(app)

    return mysql
