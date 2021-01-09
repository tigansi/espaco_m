import json
import psycopg2
import datetime

from Banco import Banco
from psycopg2.extras import RealDictCursor


class notificacao:
    def __init__(self):
        pass

    def verifica_notificacao_cliente(self):
        """
            Método que procura se há algum agendamento
            no dia para cada cliente, se caso existir,
            mostra uma notificação no celular
        """
        try:
            banco = Banco()
            curso = banco.conectar()

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul
