from cgi import print_form
from flask import Flask, render_template ,request, redirect, url_for
import config.functions as func
from config.route import route
import json

# Import config untuk konfigurasi databse
f = open('config/config.json')
# membaca data json
config = json.load(f)

#Membuat konfigurasi awal flask untuk menjalankan server  
app = Flask(__name__)
app.register_blueprint(route, url_prefix="")

# Memanggil fungsi / sintaks mysql
mysql = func.connection(app)

@app.route("/")
def main():
    return render_template("index.html", menu="main", submenu='dashboard')

@app.route("/databarang")
def databarang() :
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM barang")
    barang = cur.fetchall()
    cur.close()
    return render_template('mod_barang/databarang.html', menu="barang", submenu="listdatabarang", data=barang)

@app.route("/inputbarangproses", methods=["POST"])
def inputbarangproses():
    idbarang = request.form["idbarang"]
    namabarang = request.form["namabarang"]
    totalbarang = request.form["totalbarang"]
    hargabarang = request.form["hargabarang"]
    statusbarang = request.form["statusbarang"]
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
    return redirect(url_for('databarang'))

@app.route("/deletebarang/<string:id>", methods={"POST", "GET"})
def deletebarang(id):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM barang WHERE barang_id = %s"
    selected = (id, )
    cekID = cur.execute(query, selected)
    print(cekID)
    if (cekID > 1):
        cur.execute("DELETE FROM barang WHERE barang_id = %s", selected)
        mysql.connection.commit()
    cur.close()
    return redirect(url_for('databarang'))

if __name__ == "__main__":
    app.run(debug=True)