from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask_cors import CORS

from werkzeug.utils import secure_filename

from Usuarios import Usuarios

import os
import json
import shutil

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "index"


@app.route("/usuarios", methods=["POST"])
def usuarios():
    if(request.method == "POST"):
        data = json.loads(request.get_data())
        usuarios = Usuarios()

        if(data["tipo"] == "login"):
            return json.dumps(usuarios.login(data))

        elif(data["tipo"] == "cad_usuario"):
            return json.dumps(usuarios.cadastro_usuario(data))


if __name__ == '__main__':
    app.run(
        debug=True,
        host="192.168.8.7")
    app.config['TEMPLATES_AUTORELOAD'] = True
