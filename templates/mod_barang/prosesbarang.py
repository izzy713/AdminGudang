from flask import Blueprint, render_template, request, redirect, url_for
import config.functions as func
from config.functions import mysql

route = Blueprint("route", __name__, static_folder="../static", template_folder="../templates")

@route.route("/databarang")
def databarang() :
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM barang")
    barang = cur.fetchall()
    cur.close()
    return render_template('mod_barang/databarang.html', menu="barang", submenu="listdatabarang", data=barang)

@route.route("/inputbarang")
def inputbarang():
    return render_template("mod_barang/inputbarang.html", menu="barang", submenu="forminputbarang")

@route.route("/inputbarangproses", methods=["POST"])
def inputbarangproses():
    idbarang = request.form["idbarang"]
    namabarang = request.form["namabarang"]
    totalbarang = request.form["totalbarang"]
    hargabarang = request.form["hargabarang"]
    statusbarang = func.YesNo(request.form["statusbarang"])
    userinputbarang = request.form["userinputbarang"]
    cur = mysql.connection.cursor()
    query = "SELECT * FROM barang WHERE barang_id = %s"
    selected = (idbarang, )
    cekID = cur.execute(query, selected)
    print(cekID)
    if (cekID < 1):
        cur.execute("INSERT INTO barang(barang_id, barang_desc, barang_total, barang_price, barang_actived, barang_cdate, barang_cuser) VALUES (%s, %s, %s, %s, %s, %s, %s)", (idbarang, namabarang, totalbarang, hargabarang, statusbarang, func.datenow(), userinputbarang ))
        mysql.connection.commit()
    cur.close()
    return redirect(url_for('route.databarang'))

@route.route("/editbarang/<string:id>", methods=['GET', 'POST'])
def editbarang(id):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM barang WHERE barang_id = %s"
    selected = (id, )
    cekID = cur.execute(query, selected)
    if (cekID > 0):
        barang = cur.fetchall()
    else:
        barang = ''
    cur.close()
    total = func.SumTotal(barang[0][3], barang[0][2])
    return render_template("mod_barang/editbarang.html", menu="barang", submenu="forminputbarang" , databarang=barang, totalharga=total)

@route.route("/editbarangproses/<string:id>", methods={"POST"})
def editbarangproses(id):
    idbarang = id
    namabarang = request.form["namabarang"]
    totalbarang = request.form["totalbarang"]
    hargabarang = request.form["hargabarang"]
    statusbarang = func.YesNo(request.form["statusbarang"])
    userinputbarang = request.form["userinputbarang"]
    cur = mysql.connection.cursor()
    query = "SELECT * FROM barang WHERE barang_id = %s"
    selected = (idbarang, )
    cekID = cur.execute(query, selected)
    if (cekID >= 1):
        cur.execute("UPDATE barang SET barang_desc = %s, barang_total = %s, barang_price = %s, barang_actived = %s, barang_cdate = %s, barang_cuser = %s WHERE barang_id = %s", (namabarang, totalbarang, hargabarang, statusbarang, func.datenow(), userinputbarang, idbarang ))
        mysql.connection.commit()
    cur.close()
    return redirect(url_for('route.databarang'))

@route.route("/deletebarang/<string:id>", methods={"POST", "GET"})
def deletebarang(id):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM barang WHERE barang_id = %s"
    selected = (id, )
    cekID = cur.execute(query, selected)
    if (cekID > 0):
        querydelete = "DELETE FROM barang WHERE barang_id = %s"
        cur.execute(querydelete, selected)
        mysql.connection.commit()
    cur.close()
    return redirect(url_for('route.databarang'))