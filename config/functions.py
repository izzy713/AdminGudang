from flask_mysqldb import MySQL
from datetime import date

mysql = MySQL()

def datenow():
    today = date.today()
    return today

def YesNo(params):
    feedback = "N"

    if params == "True":
        feedback = "Y"

    return feedback

def SumTotal(harga, total):
    total = harga * total
    return total