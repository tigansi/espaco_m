import json
import psycopg2
import datetime

from Banco import Banco
from psycopg2.extras import RealDictCursor


class Avaliacao:
    def __init__(self):
        pass

    def cadastra_avaliacao(self, data: list) -> {}:
        """Método que cadastra Cadastro da avaliação"""
        try:
            banco = Banco()
            curso = banco.conectar()

            # Teste para saber qual é o tipo de avaliação
            # que será cadastrada, cliente ou colaborador

            if(data["tp"] == "COL_CLI"):
                # Colaborador avalia cliente
                sql = """INSERT
                            INTO avaliacao(
                                    id_agenda,
                                    id_colaborador,
                                    id_cliente,
                                    vl_avaliacao_cli,
                                    is_avaliado_colaborador)
                            VALUES(%s,%s, %s,%s, %s) RETURNING id_avaliacao"""

                val = (data["id_agenda"], data["id_avaliador"],
                       data["id_avaliado"], data["avaliacao"], '1')

                curso.execute(sql, val)
                id_avaliacao = curso.fetchone()
                banco.commit()

                if(data["comentarios"] != ""):
                    sql = """INSERT 
                            INTO comentarios(id_avaliacao, comentario) 
                        VALUES(%s, %s)"""

                    val = (id_avaliacao["id_avaliacao"], data["comentarios"])

                    curso.execute(sql, val)
                    banco.commit()

            elif(data["tp"] == "CLI_COL"):
                print("CLI_COL")

                print(str(data["id_avaliacao"]))
                # Cliente avalia colaborador e serviço

                sql = """UPDATE 
                            avaliacao 
                        SET 
                            vl_avaliacao_col = %s,
                            is_avaliado_cliente = '1'
                        WHERE
                            id_avaliacao = %s"""

                id_avaliacao = data["id_avaliacao"]

                print(str(id_avaliacao))
                val = (data["avaliacao"], id_avaliacao)

                curso.execute(sql, val)
                banco.commit()

                if(data["comentarios"] != ""):
                    sql = """INSERT 
                            INTO comentarios(id_avaliacao, comentario) 
                        VALUES(%s, %s)"""

                    val = (id_avaliacao, data["comentarios"])

                    curso.execute(sql, val)
                    banco.commit()

            resul = {"msg": "Avaliação cadastrada com sucesso",
                     "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def avaliacao_pendente(self, data: list) -> {}:
        """Método que procura por avaliações pendentes"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """SELECT
                        avaliacao.id_avaliacao,
	                    avaliacao.id_colaborador as id_avaliador,
	                    avaliacao.vl_avaliacao_cli avaliacao_avaliador,
	                    usuarios.id_usuario as id_avaliado,
	                    usuarios.nm_usuario as nm_avaliado,
	                    to_char(horarios.data,
	                    		 'dd/mm/YYYY HH24:MI') as data,
	                    servicos.nm_servico,
	                    servicos.valor,
                        agenda.id_agenda
                        FROM
                        	avaliacao
                        JOIN usuarios
                        ON usuarios.id_usuario = avaliacao.id_cliente
                        JOIN agenda
                        ON agenda.id_agenda = avaliacao.id_agenda AND
                           agenda.is_concluido = '1' AND
                           avaliacao.is_avaliado_cliente = '0' AND
                           avaliacao.is_avaliado_colaborador = '1' AND
                           avaliacao.id_cliente = %s
                        JOIN horarios
                        ON horarios.id_horario = agenda.id_horario
                        JOIN servicos
                        ON servicos.id_servico = horarios.id_servico"""

            val = (data["id_avaliador"], )
            curso.execute(sql, val)
            dad = curso.fetchall()

            if(len(dad) > 0):
                # Há avaliações pendentes
                resul = {"msg": "Há avaliações pendentes",
                         "dados": dad, "sucesso": True}
            else:
                # Não há
                resul = {"msg": "Não há avaliações pendentes",
                         "sucesso": False}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def avaliacao_profissional(self, data: list) -> {}:
        """Método que consulta a nota do profissional pelo seu id"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """SELECT 
                        to_char(AVG(vl_avaliacao_col)::real, '9.9') as nota
                    FROM 
                        avaliacao 
                    WHERE
                        id_colaborador = %s AND 
                        vl_avaliacao_col > 0"""

            val = (data["id_col"], )
            curso.execute(sql, val)
            dad = curso.fetchall()

            resul = {"msg": "Avaliação encontrada",
                     "dados": dad, "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul
