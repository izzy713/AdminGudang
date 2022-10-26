from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main() -> str:
    return render_template("index.html", menu="main")

@app.route("/inputbarang")
def inputbarang() -> str:
    return render_template("mod_barang/inputbarang.html", menu="barangmasuk", submenu="forminputbarang")

@app.route("/databarang")
def databarang() -> str:
    return render_template('mod_barang/databarang.html', menu="databarang", submenu="listdatabarang")

if __name__ == "__main__":
    app.run(debug=False)