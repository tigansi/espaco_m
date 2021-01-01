import json
import psycopg2
import datetime

from Banco import Banco
from psycopg2.extras import RealDictCursor


class Avaliacao:
    def __init__(self):
        pass

    def cadastra_avaliacao(self, data:list) -> {}:
        """Método que cadastra Cadastro da avaliação"""
        try:
            banco = Banco()
            curso = banco.conectar()

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

        pass
