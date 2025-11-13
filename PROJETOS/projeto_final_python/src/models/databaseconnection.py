from functools import cache
import mysql.connector, sqlite3, pymysql
from dotenv import load_dotenv
import os

load_dotenv("src\config\.env")
PASSWORD_DB = os.getenv("PASSWORD_DB")

@cache
class DatabaseConnection:
    def __init__(self, db_type, **kwargs):
        self.db_type = db_type
        self.connection = None
        self.cursor = None
        self.config = kwargs

    def connect(self):
        try:
            if self.db_type == "sqlite":
                self.connection = sqlite3.connect(self.config.get("database"))
            elif self.db_type == "mysql":
                self.connection = mysql.connector.connect(
                    host=self.config.get("host"),
                    user=self.config.get("user"),
                    password=self.config.get("password"),
                    database=self.config.get("database")
                )
            elif self.db_type == "pymysql":
                self.connection = pymysql.connect(
                    host=self.config.get("host"),
                    user=self.config.get("user"),
                    password=self.config.get("password"),
                    database=self.config.get("database")
                )
            else:
                raise ValueError("Tipo de banco de dados não suportado.")
            self.cursor = self.connection.cursor()
            print(f"Conexão com {self.db_type} bem sucedida!")
        except Exception as e:
            print(f"Erro ao conectar: {e}")

    def execute(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print("Query executada com sucesso!")
        except Exception as e:
            print(f"Erro ao executar query: {e}")

    def fetch_all(self):
        try:
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")
            return None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexão encerrada.")

db_pysql = DatabaseConnection(db_type="pymysql", host="localhost", user="root", password=PASSWORD_DB, database="loja")

# Exemplo de uso com SQLite
# db = DatabaseConnection("sqlite", database="meu_banco.db")
# db.connect()
# db.execute_query("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
# db.execute_query("INSERT INTO usuarios (nome) VALUES (?)", ("João",))
# db.execute_query("SELECT * FROM usuarios")
# print(db.fetch_all())
# db.close()
        