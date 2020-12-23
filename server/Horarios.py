import json
import psycopg2
import datetime

from Banco import Banco
from psycopg2.extras import RealDictCursor


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

            for i in data["hor_selecionados"]:
                # data que irá para o banco em forma de string
                data_banco_string = str(data["dia"]) + " " + str(i)
                # Formato que será guardado
                data_banco_format = '%Y-%m-%d %H:%M'
                # Conversão para o formato do Python
                data_banco_python = datetime.datetime.strptime(
                    data_banco_string, data_banco_format)

                # Query do banco
                sql = """INSERT 
                            INTO horarios(id_servico, 
                                          id_usuario,
                                          data)
                            VALUES(%s, %s, %s)"""

                val = (data["servico"],
                       data["id_usuario"], data_banco_python)

                curso.execute(sql, val)
                banco.commit()

            resul = {
                "msg": "Cadastro realizado com sucesso",
                "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def lista_horarios(self, data: list) -> {}:
        """Método que lista os horários cadastrados para o usuário"""
        try:
            banco = Banco()
            curso = banco.conectar()

            # Serve para ajuste da data de nascimento
            PARAM_DATA = str("dd/mm/YYYY HH24:MI")

            sql = """SELECT 
                        horarios.id_horario as id_horario,
                        horarios.id_servico as id_servico, 
                        horarios.id_usuario as id_usuario,
                        to_char(horarios.data, %s) as data,
                        horarios.is_ativo as is_ativo,
                        servicos.nm_servico as nm_servico
                    FROM 
                        horarios
                    INNER JOIN servicos ON
                        horarios.id_servico = servicos.id_servico AND
                        horarios.id_usuario = %s AND
                        horarios.data >= current_timestamp
                    ORDER BY horarios.data asc"""

            val = (PARAM_DATA, data["id_usuario"])
            curso.execute(sql, val)
            dad = curso.fetchall()

            if(len(dad) > 0):
                resul = {"msg": "Há horários",
                         "sucesso": True, "dados": dad}
            else:
                resul = {"msg": "Não há horários disponíveis", "sucesso": False}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def monta_grade_horarios(self, data: list) -> {}:
        """Método que monta a grade de horários"""

        try:
            banco = Banco()
            curso = banco.conectar()

            """
            Esse método é responsável por montar a tabela de
            horários para o usuário no aplicativo. Ela é montada
            com base nos tempos de cada procedimento. Antes de 
            preparar a lista de horários, o algoritmo faz algumas
            análises. A primeira delas é com relação ao passado,
            a agenda só será montada com horários acima do horário atual,
            além disso, existe uma trava para que a lista não ultrapasse
            o horário limite do salão. Por fim é feita uma validação no banco
            para saber o horário já não usado em outro procedimento
            """

            # Lista de horas, é onde terá os horários para o usuário escolher
            list_horas = list()
            # Variável que armazena o agora para fazer a trava
            hoje_str = datetime.datetime.now()
            # Conversão da variável de trava
            hoje_fmt = hoje_str.strftime("%d/%m/%Y %H:%M")
            # Variável que armazena o horário de abertura do salão
            dia_string = str(data["dia"]) + " " + "08:00"
            # Conversão da variável de horário de abertura
            dia_formtt = '%Y-%m-%d %H:%M'
            # Variável que armazena a data no formato do Python
            dia_fmtpyt = datetime.datetime.strptime(dia_string, dia_formtt)
            # Variável que armazena a data com o horário de fechamento
            datf_string = str(data["dia"]) + " " + "18:00"
            # Conversão da variável de horário de fechamento
            datf_formtt = '%Y-%m-%d %H:%M'
            # Variável que armazena a data no formato do Python
            datf_fmtpyt = datetime.datetime.strptime(datf_string, datf_formtt)

            # Contador de durações
            cont = 0
            # Loop para teste e armazenamento
            for i in range(1, 15):
                # Acumulador de durações
                cont += int(data["duracao"])
                # Soma dos minutos com base na duração do procedimento
                mint = dia_fmtpyt + datetime.timedelta(minutes=cont)
                # Formatação da data que os minutos foram somados
                dat = mint.strftime("%d/%m/%Y %H:%M")

                # O primeiro teste é para não deixar mostrar os horários passados
                # Já o segundo, é para não deixar mostrar os horários após o fechamento
                if(dat >= hoje_fmt and dat <= datf_fmtpyt.strftime("%d/%m/%Y %H:%M")):
                    # Agora é o momento em que acontece a verificação da data no banco
                    sql = """SELECT * FROM horarios 
                                WHERE id_usuario = %s AND data = %s"""

                    val = (data["id_usuario"], dat)
                    curso.execute(sql, val)
                    dados = curso.fetchall()

                    if(len(dados) == 0):
                        # Armazenamento dos horários elegíveis
                        list_horas.append(mint.strftime("%H:%M"))
                    else:
                        print("Horário: " + str(dat) + " Já cadastrado")

                # Verifica se há horários, caso não haja, será informado ao usuário
                if(len(list_horas) > 0):
                    resul = {
                        "msg": "Grade montada com sucesso",
                        "sucesso": True, "dados": list_horas}
                else:
                    resul = {
                        "msg": "Não há mais horários disponíveis para esse dia",
                        "sucesso": False}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def limpa_horarios(self, data: list) -> {}:
        """Método responsável """
        pass

    def deleta_horarios(self, data: list) -> {}:
        """Método que exclui o horário escolhido pelo colaborador"""
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """DELETE FROM 
                        horarios 
                    WHERE 
                        id_horario = %s AND 
                        is_ativo = '1'"""

            val = (data["id_hor"], )
            curso.execute(sql, val)
            banco.commit()

            resul = {"msg": "Horário excluido com sucesso", "sucesso": True}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def lista_serv_prof(self, data: list) -> {}:
        """
        Método que lista os serivços em que o profissional tem
        algum horário cadastrado
        """
        try:
            banco = Banco()
            curso = banco.conectar()

            sql = """SELECT 
                        DISTINCT ON (servicos.id_servico)
                        servicos.id_servico,
                        servicos.valor,
                        servicos.nm_servico
                    FROM
	                    servicos
                    INNER JOIN 
	                    horarios on 
		                    servicos.id_servico = horarios.id_servico AND
		                    horarios.id_usuario = %s AND
                            data >= current_timestamp"""

            val = (data["id_col"], )
            curso.execute(sql, val)
            dad = curso.fetchall()

            resul = {"msg": "Serviço achados",
                     "sucesso": True, "dados": dad}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul

    def list_hor_serv_prof(self, data: list):
        """"""
        try:
            banco = Banco()
            curso = banco.conectar()

            print(data["dia"])

            # Teste para ver se a data passa a hora de trava(18:00)
            # Variável que armazena o agora para fazer a trava
            hoje_str = datetime.datetime.now()
            # Conversão da variável de trava
            hoje_fmt = hoje_str.strftime("%Y-%m-%d %H:%M")
            # Variável que armazena a data com o horário de fechamento
            datf_string = str(data["dia"]) + " " + "18:00"
            # Conversão da variável de horário de fechamento
            datf_formtt = '%Y-%m-%d %H:%M'
            # Variável que armazena a data no formato do Python
            datf_fmtpyt = datetime.datetime.strptime(datf_string, datf_formtt)

            # Verificado se o salão ainda está aberto
            if(hoje_fmt <= datf_fmtpyt.strftime('%Y-%m-%d %H:%M')):
                sql = """SELECT
	                        horarios.id_horario,
                            to_char(horarios.data, 'HH24:MI') as data
                        FROM 
                        	horarios
                        WHERE 
	                        horarios.id_usuario = %s AND
                            horarios.id_servico = %s AND
                            horarios.data::date = date %s
                        ORDER BY horarios.data asc"""

                val = (data["id_usuario"], data["id_servico"], data["dia"])
                curso.execute(sql, val)
                dad = curso.fetchall()

                if(len(dad) > 0):
                    resul = {"msg": "Há horários disponíveis",
                             "sucesso": True, "dados": dad}
                else:
                    resul = {"msg": "Não há horários disponíveis",
                             "sucesso": False}
            else:
                resul = {"msg": "Não há horários disponíveis",
                         "sucesso": False}

        except (Exception, psycopg2.Error) as error:
            resul = {"msg": str(error), "sucesso": False}

        curso.close()
        banco.fechar()

        print(resul)
        return resul
