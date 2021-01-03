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

    def list_agenda_prof(self, data: list) -> {}:
        """Método que Lista a agenda do profissional"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """SELECT
	                    agenda.id_agenda,
	                    agenda.id_cliente,
                        agenda.is_andamento,
	                    usuarios.nm_usuario as nm_cliente,
                        usuarios.foto,
	                    to_char(horarios.data,
		                    'dd/mm/YYYY HH24:MI') as data,
	                    servicos.nm_servico
                    FROM agenda
                    JOIN usuarios
                    ON agenda.id_cliente = usuarios.id_usuario AND
                       agenda.is_ativo = '1'
                    JOIN horarios
                    ON agenda.id_horario = horarios.id_horario AND
                       horarios.data >= current_timestamp AND
                       horarios.id_usuario = %s
                    JOIN servicos
                    ON horarios.id_servico = servicos.id_servico"""

            val = (data["id_col"], )
            curso.execute(sql, val)
            dad = curso.fetchall()

            resul = {"msg": "Dados encontrados", "sucesso": True, "dados": dad}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def list_agenda_cli(self, data: list) -> {}:
        """Método que Lista a agenda do cliente"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """SELECT
	                    agenda.id_agenda,
	                    agenda.id_cliente,
                        agenda.is_andamento,
	                    usuarios.nm_usuario,
                        usuarios.foto,
	                    to_char(horarios.data,
		                    'dd/mm/YYYY HH24:MI') as data,
	                    servicos.nm_servico,
                        horarios.id_horario
                    FROM agenda
                        JOIN horarios
                        ON agenda.id_horario = horarios.id_horario AND
                           horarios.data >= current_timestamp AND
                           agenda.is_concluido = '0'
                        JOIN servicos
                        ON horarios.id_servico = servicos.id_servico
                        JOIN usuarios
                        ON horarios.id_usuario = usuarios.id_usuario"""

            val = (data["id_usuario"], )
            curso.execute(sql, val)
            dad = curso.fetchall()

            resul = {"msg": "Dados encontrados", "sucesso": True, "dados": dad}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def inicia_serv(self, data: list) -> {}:
        """Método que dá inicio ao serviço"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """UPDATE
                        agenda
                    SET
                        is_andamento = '1'
                    WHERE id_agenda = %s"""

            val = (data["id_agenda"], )
            curso.execute(sql, val)
            banco.commit()

            resul = {"msg": "Serviço iniciado", "sucesso": True}
        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def para_serv(self, data: list) -> {}:
        """Método que para o serviço"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """UPDATE 
                        agenda 
                    SET 
                        is_andamento = '0' 
                    WHERE id_agenda = %s"""

            val = (data["id_agenda"], )
            curso.execute(sql, val)
            banco.commit()

            resul = {"msg": "Serviço parado", "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def conclui_serv(self, data: list()) -> {}:
        """Método que conclui o servico"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """UPDATE 
                        agenda 
                    SET 
                        is_concluido = '1',
                        is_andamento = '0',
                        is_ativo = '0'
                    WHERE id_agenda = %s"""

            val = (data["id_agenda"], )
            curso.execute(sql, val)
            banco.commit()

            resul = {"msg": "Serviço parado", "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def desiste_agenda(self, data: list) -> {}:
        """Método que apaga a agenda e horário selecionado"""
        try:
            banco = Banco()
            curso = banco.conectar()

            # O registro deve ser excluido da tabela de agenda
            # Depois marcar o horário como disponível na tabela

            sql = """DELETE 
                        FROM agenda 
                    WHERE id_agenda = %s"""

            val = (data["id_agenda"], )
            curso.execute(sql, val)
            banco.commit()

            sql = """UPDATE horarios 
                        SET is_ativo = '1'
                    WHERE id_horario = %s"""

            val = (data["id_horario"], )
            curso.execute(sql, val)
            banco.commit()

            resul = {"msg": "Agenda excluida com sucesso", "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul
