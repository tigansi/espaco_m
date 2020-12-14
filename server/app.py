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

UPLOAD_PATH = './Fotos'
app.config['UPLOAD_PATH'] = UPLOAD_PATH


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

        elif(data["tipo"] == "lista_colaboradores"):
            return json.dumps(usuarios.lista_colaboradores(data))

        elif(data["tipo"] == "desliga_user"):
            pass


@app.route("/altera_dados", methods=["POST"])
def altera_dados():
    if(request.method == "POST"):
        # Instância do objeto
        usuarios = Usuarios()

        # É necessário saber antes de tudo se o usuário
        # informou alguma foto para alteração
        if('foto_user' not in request.files):
            # Não há foto
            data = json.loads(request.form["dados"])
            return json.dumps(usuarios.altera_dados(data, ""))
        else:
            # Há foto
            # Variável com o dados do usuario
            data = json.loads(request.form["dados"])

            # Armazenamento do envio
            file = request.files["foto_user"]

            # Tratamento de segurança
            filename = secure_filename(file.filename)

            # Verificação se a pasta nomeada com o id já existe
            # Caso exista, será verificado o que tem dentro pra fazer a
            # exclusão e depois o armazenamento da nova foto, caso contrário
            # Será criada a pasta onde ficará a foto do usuário
            # Por conseguinte, os dados serão alterados

            if(not(os.path.exists("./Fotos/" + str(data["id"])))):
                os.mkdir("./Fotos/" + str(data["id"]))
                file.save(os.path.join(
                    app.config['UPLOAD_PATH'] + "/" + str(data["id"]), filename))

            else:
                dir = os.listdir("./Fotos/" + str(data["id"]))
                for arq in dir:
                    os.remove("./Fotos/" + str(data["id"]) + "/" + str(arq))

                file.save(os.path.join(
                    app.config['UPLOAD_PATH'] + "/" + str(data["id"]), filename))

                caminho = app.config['UPLOAD_PATH'] + \
                    '/' + str(data['id']) + "/" + str(filename)

                return json.dumps(usuarios.altera_dados(data, caminho))


@app.route("/fotos", methods=["GET"])
def fotos():
    if(request.method == "GET"):
        cam = request.args.get("caminho")

        if(cam == "./Fotos/avatar.png"):
            return send_file(cam, mimetype='image/png', cache_timeout=0)
        else:
            return send_file(cam, mimetype='image/jpg', cache_timeout=0)


if __name__ == '__main__':
    app.run(
        debug=True,
        host="192.168.8.7")
    app.config['TEMPLATES_AUTORELOAD'] = True
