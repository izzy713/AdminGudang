from flask import Flask, render_template
import config.functions as func
from templates.mod_barang.prosesbarang import route
import json

#Membuat konfigurasi awal flask untuk menjalankan server  
app = Flask(__name__)
app.register_blueprint(route, url_prefix="")

f = open('config/config.json')
config = json.load(f)

app.config['MYSQL_HOST'] = config['system_localhost']
app.config['MYSQL_USER'] = config['system_username']
app.config['MYSQL_PASSWORD'] = config['system_password']
app.config['MYSQL_DB'] = config['system_database']
func.mysql.init_app(app)
    
@app.route("/")
def main():
    return render_template("index.html", menu="main", submenu='dashboard')

@app.route("/datateam/")
def datateam():
    return render_template("mod_team/datateam.html", menu="teams", submenu="listeam")

if __name__ == "__main__":
    app.run(debug=True)