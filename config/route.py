from flask import Blueprint, render_template

route = Blueprint("route", __name__, static_folder="../static", template_folder="../templates")

@route.route("/inputbarang")
def inputbarang():
    return render_template("mod_barang/inputbarang.html", menu="barang", submenu="forminputbarang")
