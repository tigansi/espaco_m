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
                                    id_avaliado,
                                    id_avaliador,
                                    vl_avaliacao_cli,
                                    comentarios_cli,
                                    is_avaliado_colaborador)
                            VALUES(%s,%s, %s,%s, %s,%s)"""

                val = (data["id_agenda"], data["id_avaliado"],
                       data["id_avaliador"], data["avaliacao"],
                       data["comentarios"], '1')

            elif(data["tp"] == "CLI_COL"):
                # Cliente avalia colaborador e serviço
                # Nesse caso, ao invés de ser um insert,
                # deve ser feito um Update

                sql = """UPDATE 
                            avaliacao 
                        SET 
                            vl_avaliacao_col = %s,
                            is_avaliado_cliente = '1',
                            comentarios_col = %s
                        WHERE
                            id_avaliacao = %s"""

                val = (data["avaliacao"],  data["comentarios"],
                       data["id_avaliacao"])

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
	                    avaliacao.id_avaliado as id_avaliador,
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
                        ON usuarios.id_usuario = avaliacao.id_avaliador
                        JOIN agenda
                        ON agenda.id_agenda = avaliacao.id_agenda AND
                           agenda.is_concluido = '1' AND
                           avaliacao.is_avaliado_cliente = '0' AND
                           avaliacao.is_avaliado_colaborador = '1' AND
                           avaliacao.id_avaliado = %s
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
