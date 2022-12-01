from flask import Blueprint, render_template
from config.functions import mysql

routelogs = Blueprint("routelogs", __name__, static_folder="../static", template_folder="../templates")

@routelogs.route("/datalogs")
def datalogs() :
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM logs")
    datalogs = cur.fetchall()
    cur.close()
    return render_template('mod_logs/datalogs.html', menu="admin", submenu="listdatalogs", data=datalogs)