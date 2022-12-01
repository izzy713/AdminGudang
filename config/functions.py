from flask_mysqldb import MySQL
from datetime import datetime

mysql = MySQL()

def datenow():
    today = datetime.now()
    return today

def YesNo(params):
    feedback = "N"
    if params == "True":
        feedback = "Y"
    return feedback

def SumTotal(harga, total):
    total = harga * total
    return total

def Logs(table, params, data):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO logs(logs_table, logs_params, logs_data, logs_cuser, logs_cdate) VALUES (%s, %s, %s, %s, %s)", (table, params, data, 'system', datenow()))
    mysql.connection.commit()
    print("aa")