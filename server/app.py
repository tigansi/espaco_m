from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask_cors import CORS

from werkzeug.utils import secure_filename

from Usuarios import Usuarios
from Servicos import Servicos
from Horarios import Horarios
from Agenda import Agenda
from Avalicao import Avaliacao

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
            print("há foto")
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

                caminho = app.config['UPLOAD_PATH'] + \
                    '/' + str(data['id']) + "/" + str(filename)

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


@app.route("/categorias", methods=["POST"])
def categorias():
    if(request.method == "POST"):
        data = json.loads(request.get_data())
        serv = Servicos()
        if(data["tipo"] == "cad_cat"):
            return json.dumps(serv.cadastra_categoria(data))

        elif(data["tipo"] == "list_cat"):
            return json.dumps(serv.lista_categorias())

        elif(data["tipo"] == "del_cat"):
            return json.dumps(serv.desativa_categoria(data))


@app.route("/servicos", methods=["POST"])
def servicos():
    if(request.method == "POST"):
        data = json.loads(request.get_data())
        serv = Servicos()
        if(data["tipo"] == "cad_serv"):
            return json.dumps(serv.cadastra_servicos(data))

        elif(data["tipo"] == "list_serv"):
            return json.dumps(serv.lista_servicos())

        elif(data["tipo"] == "del_serv"):
            return json.dumps(serv.desativa_servico(data))


@app.route("/horarios", methods=["POST"])
def horarios():
    if(request.method == "POST"):
        data = json.loads(request.get_data())
        hora = Horarios()
        if(data["tipo"] == "cad_hor"):
            return json.dumps(hora.cadastra_horario(data))

        elif(data["tipo"] == "monta_grad_hor"):
            return json.dumps(hora.monta_grade_horarios(data))

        elif(data["tipo"] == "list_hor"):
            return json.dumps(hora.lista_horarios(data))

        elif(data["tipo"] == "limpa_hor"):
            return json.dumps(hora.limpa_horarios(data))

        elif(data["tipo"] == "deleta_hor"):
            return json.dumps(hora.deleta_horarios(data))

        elif(data["tipo"] == "lista_serv_prof"):
            return json.dumps(hora.lista_serv_prof(data))

        elif(data["tipo"] == "lista_prof_serv"):
            return json.dumps(hora.lista_prof_serv(data))

        elif(data["tipo"] == "list_hor_serv_prof"):
            return json.dumps(hora.list_hor_serv_prof(data))


@app.route("/agenda", methods=["POST"])
def agenda():
    if(request.method == "POST"):
        data = json.loads(request.get_data())
        agenda = Agenda()
        if(data["tipo"] == "agenda_hor"):
            return json.dumps(agenda.agenda_horario(data))

        elif(data["tipo"] == "list_agenda_prof"):
            return json.dumps(agenda.list_agenda_prof(data))

        elif(data["tipo"] == "list_agenda_cli"):
            return json.dumps(agenda.list_agenda_cli(data))

        elif(data["tipo"] == "inicia_serv"):
            return json.dumps(agenda.inicia_serv(data))

        elif(data["tipo"] == "para_serv"):
            return json.dumps(agenda.para_serv(data))

        elif(data["tipo"] == "conclui_serv"):
            return json.dumps(agenda.conclui_serv(data))

        elif(data["tipo"] == "desiste_agenda"):
            return json.dumps(agenda.desiste_agenda(data))


@app.route("/avaliacao", methods=["POST"])
def avaliacao():
    if(request.method == "POST"):
        data = json.loads(request.get_data())
        avaliacao = Avaliacao()

        if(data["tipo"] == "cad_aval"):
            return json.dumps(avaliacao.cadastra_avaliacao(data))

        elif(data["tipo"] == "aval_pend"):
            return json.dumps(avaliacao.avaliacao_pendente(data))


if __name__ == '__main__':
    app.run(
        debug=True,
        host="192.168.8.7")
    app.config['TEMPLATES_AUTORELOAD'] = True
