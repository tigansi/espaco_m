import psycopg2
from psycopg2.extras import RealDictCursor


class Banco:
    def __init__(self):
        self.host = "localhost"
        self.user = "postgres"
        self.datb = "espaco_m"
        self.pasw = "root"
        self.conn = ""

    def conectar(self):
        self.conn = psycopg2.connect(
            host=str(self.host), database=str(self.datb),
            user=str(self.user), password=str(self.pasw))

        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        return cursor

    def fechar(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()
