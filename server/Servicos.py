import json
import psycopg2

from Banco import Banco
from psycopg2.extras import RealDictCursor


class Servicos:
    def __init__(self):
        pass

    def cadastra_categoria(self, data: list) -> {}:
        """Método que cadastra a categoria do serviço"""
        try:
            banco = Banco()
            curso = banco.conectar()

            # Verificar se já não existe uma categoria com
            # mesmo nome, pois se existir será informado ao usuário

            sql = """SELECT * FROM categorias WHERE nm_categoria = %s"""
            val = (data["nm_cat"], )

            curso.execute(sql, val)
            if(len(curso.fetchall()) > 0):
                resul = {"msg": "Categoria já cadastrada",
                         "sucesso": False}
            else:
                sql = """INSERT
                            INTO categorias(nm_categoria)
                        VALUES(%s)"""

                val = (str(data["nm_cat"]), )
                curso.execute(sql, val)
                banco.commit()

                resul = {"msg": "Categoria cadastrada",
                         "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def lista_categorias(self) -> {}:
        """Método responsável pela listagem das categorias"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """SELECT 
                        id_categoria,
                        nm_categoria
                    FROM 
                        categorias
                    WHERE 
                        is_ativo = '1'"""

            curso.execute(sql)
            dad = curso.fetchall()

            resul = {"msg": "Carregamento realizado",
                     "sucesso": True, "dados": dad}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def desativa_categoria(self, data: list) -> {}:
        """Método que desativa as categorias selecionadas"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """UPDATE 
                        categorias 
                    SET 
                        is_ativo = '0' 
                    WHERE 
                        id_categoria = %s"""

            val = (str(data["id"]), )
            curso.execute(sql, val)
            banco.commit()

            resul = {"msg": "Categoria desativada com sucesso",
                     "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def cadastra_servicos(self, data: list) -> {}:
        """Método que cadastra os serviços do salão"""
        try:
            banco = Banco()
            curso = banco.conectar()

            # Verificar se já não existe, caso exista,
            # informa ao usuário

            sql = """SELECT * FROM 
                        servicos WHERE nm_servico = %s"""

            val = (str(data["nm_servico"]), )
            curso.execute(sql, val)

            if(len(curso.fetchall()) > 0):
                resul = {"msg": "Serviço já cadastrado",
                         "sucesso": False}
            else:
                sql = """INSERT 
                            INTO 
                                servicos(nm_servico,
                                         categoria,
                                         duracao,
                                         valor)
                            VALUES(%s, %s, %s,%s)"""

                val = (str(data["nm_servico"]), str(data["nm_categoria"]),
                       str(data["duracao"]), str(data["valor"]))

                curso.execute(sql, val)
                banco.commit()

                resul = {"msg": "Serviço cadastrado com sucesso",
                         "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def lista_servicos(self):
        """Método que lista os serviços ativos do salão"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """SELECT
                        id_servico,
                        nm_servico,
                        categoria,
                        duracao,
                        valor
                    FROM 
                        servicos
                    WHERE 
                        is_ativo = '1'"""

            curso.execute(sql)
            dad = curso.fetchall()

            resul = {"msg": "Carregamento realizado",
                     "sucesso": True, "dados": dad}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def desativa_servico(self, data: list) -> {}:
        """Método que desativa o serviço selecionado"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """UPDATE 
                        servicos 
                    SET
                        is_ativo = '0'
                    WHERE 
                        id_servico = %s"""

            val = (str(data["id"]), )
            curso.execute(sql, val)
            banco.commit()

            resul = {"msg": "Serviço desativado com sucesso",
                     "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul
