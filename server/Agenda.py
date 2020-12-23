import json
import psycopg2
import datetime

from Banco import Banco
from psycopg2.extras import RealDictCursor


class Agenda:
    def __init__(self):
        pass

    def agenda_horario(self, data: list) -> {}:
        """Método que agenda o horário no banco"""
        try:
            banco = Banco()
            curso = banco.conectar()

            # Em primeiro lugar, é necessário cadastrar os dados
            # Depois, na tabela de horários, o horário deve ser alterado
            # para is_ativo = 'false'

            sql = """INSERT 
                        INTO agenda(id_horario,
                                    id_cliente)
                        VALUES(%s, %s)"""

            val = (data["id_hor"], data["id_cli"])
            curso.execute(sql, val)
            banco.commit()

            sql = """UPDATE 
                        horarios 
                    SET 
                        is_ativo = '0'
                    WHERE
                        id_horario = %s"""

            val = (data["id_hor"], )
            curso.execute(sql, val)
            banco.commit()

            resul = {"msg": "Horário agendado com sucesso", "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul
