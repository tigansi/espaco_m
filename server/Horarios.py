import json
import psycopg2


from Banco import Banco
from datetime import date
from datetime import datetime
from datetime import timedelta
from psycopg2.extras import RealDictCursor

import time


class Horarios:
    def __init__(self):
        pass

    def cadastra_horario(self, data: list) -> {}:
        """
        Método que cadastra os horários do
        colaborador
        """

        try:
            banco = Banco()
            curso = banco.conectar()

            """
            Em primeiro lugar, é necessário verificar
            se o horário informado é valido, por exemplo,
            não pode ser um horário do passado. Além disso,
            deve ser visto se o horário respeita o tempo
            do serviço, por exemplo, se um corte demora 1h,
            o próximo horário deve ser 1h adiante. Deve ser
            analisado também se aquele horário já não está selecionado
            ou se já não existe para outro serviço
            """

            self.teste_hora()

            # Armezado o dia de hoje "%Y-%m-%d %H:%M"
            hoje = datetime.now()
            # Variável formatada
            hoje = hoje.strftime("%Y-%m-%d %H:%M")
            # Varável formatada, vindo do app
            datf = data["data"].replace('T', " ")

            if(datf < hoje):
                resul = {
                    "msg": "Data inválida, por se tratar de ser passado",
                    "sucesso": False}

            else:
                sql = """SELECT * FROM horarios WHERE data = %s"""
                val = (str(datf), )
                curso.execute(sql, val)

                if(len(curso.fetchall()) > 0):
                    # Esse horário existe no banco
                    resul = {
                        "msg": "Horário já cadastrado",
                        "sucesso": False}

                else:
                    # Esse horário não existe no banco
                    # Então pode ser cadastrado
                    sql = """INSERT INTO
                                    horarios(id_servico,
                                             id_usuario,
                                             data)
                                    VALUES(%s, %s, %s)"""

                    val = (str(data["servico"]),
                           str(data["id_usuario"]), str(datf), )

                    curso.execute(sql, val)
                    banco.commit()

                    resul = {
                        "msg": "Horário cadastrado com sucesso",
                        "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def lista_horarios(self) -> {}:
        """Método que lista os horários cadastrados para o usuário"""
        try:
            banco = Banco()
            curso = banco.conectar()

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def teste_hora(self):
        data1 = '16/12/2020 07:30'
        data2 = '16/12/2020 08:00'
        
        dt1 = datetime.strptime(data1, '%d/%m/%Y %H:%M').date()
        dt2 = datetime.strptime(data2, '%d/%m/%Y %H:%M').date()

        print('Data ' + str(dt1))