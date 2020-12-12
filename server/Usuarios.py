import json
import hashlib
import psycopg2


from Banco import Banco
from psycopg2.extras import RealDictCursor


class Usuarios:
    def __init__(self):
        pass

    def cadastro_usuario(self, data: list) -> {}:
        """Método que faz a inclusão de usuários no banco"""
        try:
            banco = Banco()
            curso = banco.conectar()

            """
            Em primeiro lugar é necessário verificar se o
            usuário já não existe no banco, será feita
            uma pesquisa com o e-mail já que ele é a chave
            """

            sql = """SELECT
                        id_usuario,
                        email
                    FROM
                        usuarios
                    WHERE
                        email = %s"""

            val = (data["email"], )
            curso.execute(sql, val)

            if(len(curso.fetchall()) > 0):
                """Já existe o cadastro"""
                resul = {
                    "msg": "Já existe um usuário cadastrado com esse e-mail",
                    "sucesso": False}
            else:
                """
                É um usuário com e-mail novo, então agora
                o cadastro é realizado
                """

                # A senha será gravada no banco de forma criptografada
                senha_cript = hashlib.md5(
                    data["senha"].encode('utf8')).hexdigest()

                sql = """INSERT
                            INTO
                        usuarios(
                            nm_usuario,
                            email,
                            celular,
                            aniversario,
                            senha)
                        VALUES(%s, %s, %s, %s, %s)"""

                val = (data["nome"], data["email"], data["celular"],
                       data["aniversario"], senha_cript)

                curso.execute(sql, val)
                banco.commit()

                resul = {
                    "msg": "Usuário cadastrado com sucesso",
                    "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def login(self, data: list):
        """Método que verifica se o usuário existe no login"""

        try:
            banco = Banco()
            curso = banco.conectar()

            """
            Se o usuário existir no banco será enviado todos os dados
            dele para serem armazenados no javascript, caso contrário,
            será informado o erro
            """

            # Serve para ajuste da data de nascimento
            PARAM_DATA = str("dd/mm/YYYY")

            sql = """SELECT  
                        id_usuario,
                        nm_usuario,
                        email,   
                        to_char(aniversario, %s) as aniversario,   
                        celular,
                        tipo                
                    FROM 
                        usuarios 
                    WHERE 
                        email = %s AND 
                        senha = %s"""

            # A senha tem que ser criptografada para ser vista no banco
            senha_cript = hashlib.md5(
                data["senha"].encode('utf8')).hexdigest()

            val = (PARAM_DATA, data["email"], senha_cript)
            curso.execute(sql, val)
            dad = curso.fetchall()

            print(dad)

            if(len(dad) > 0):
                """O usuário existe"""
                resul = {"msg": "Bem vindo",
                         "dados": dad, "sucesso: ": True}
            else:
                """O usuário não existe"""
                resul = {"msg": "Usuário não encontrado",  "sucesso: ": False}
        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul
