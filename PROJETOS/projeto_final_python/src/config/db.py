import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD_DB = os.getenv("PASSWORD_DB")

con = pymysql.connect(
    host="localhost",
    user="root",
    password=PASSWORD_DB,
    database="loja"
    )

cursor = con.cursor()

# print("Conexão com banco de dados bem sucedida!")

