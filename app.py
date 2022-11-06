from cgi import print_form
from flask import Flask, render_template ,request, redirect, url_for
import config.functions as func
from config.route import route

#Membuat konfigurasi awal flask untuk menjalankan server  
app = Flask(__name__)
app.register_blueprint(route, url_prefix="/datateam")

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
    abc = [0,1,2,3,4,5,6,7,8,9]
    return render_template('mod_barang/databarang.html', menu="barang", submenu="listdatabarang", data=barang, rowdata=abc)

@app.route("/editbarang/<string:id>", methods=['GET', 'POST'])
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
    return render_template("mod_barang/editbarang.html", menu="barang", submenu="forminputbarang" , databarang=barang)

@app.route("/inputbarang")
def inputbarang():
    return render_template("mod_barang/inputbarang.html", menu="barang", submenu="forminputbarang")

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
    if (cekID > 0):
        querydelete = "DELETE FROM barang WHERE barang_id = %s"
        cur.execute(querydelete, selected)
        mysql.connection.commit()
    cur.close()
    return redirect(url_for('databarang'))

@app.route("/editbarangproses", methods={"POST"})
def editbarangproses():
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
    if (cekID >= 1):
        cur.execute("UPDATE barang SET barang_desc = %s, barang_total = %s, barang_price = %s, barang_actived = %s, barang_cdate = %s, barang_cuser = %s WHERE barang_id = %s", (namabarang, totalbarang, hargabarang, statusbarang, func.datenow(), userinputbarang, idbarang ))
        mysql.connection.commit()
    cur.close()
    return redirect(url_for('databarang'))

if __name__ == "__main__":
    app.run(debug=True)