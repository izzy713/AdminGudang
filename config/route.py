from flask import Blueprint, render_template

route = Blueprint("route", __name__, static_folder="../static", template_folder="../templates")

@route.route("/")
def datateam():
    return render_template("mod_team/datateam.html")
