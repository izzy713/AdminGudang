from flask import Flask, render_template
import config.functions as function

# print(function.coba())

app = Flask(__name__)

@app.route("/main")
def main() -> str:
    return render_template("index.html", menu="main", submenu='dashboard')

@app.route("/inputbarang")
def inputbarang() -> str:
    return render_template("mod_barang/inputbarang.html", menu="barang", submenu="forminputbarang")

@app.route("/databarang")
def databarang() -> str:
    return render_template('mod_barang/databarang.html', menu="barang", submenu="listdatabarang")

if __name__ == "__main__":
    app.run(debug=False)