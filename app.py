from cgi import print_form
from flask import Flask, render_template ,request, redirect, url_for
from flask_mysqldb import MySQL
import config.functions as func
import json

# Import config untuk konfigurasi databse
f = open('config/config.json')
# membaca data json
config = json.load(f)

#Membuat konfigurasi awal flask untuk menjalankan server  
app = Flask(__name__)

# konfigurasi database
app.config['MYSQL_HOST'] = config['system_localhost']
app.config['MYSQL_USER'] = config['system_username']
app.config['MYSQL_PASSWORD'] = config['system_password']
app.config['MYSQL_DB'] = config['system_database']

# Memanggil fungsi / sintaks mysql
mysql = MySQL(app)

@app.route("/")
def main():
    return render_template("index.html", menu="main", submenu='dashboard')

@app.route("/inputbarang")
def inputbarang():
    return render_template("mod_barang/inputbarang.html", menu="barang", submenu="forminputbarang")

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

if __name__ == "__main__":
    app.run(debug=True)