from utils.__init__ import con, cursor, Produto
import keyboard
from time import sleep

def retornar_produtos(listar_produtos: bool=False):
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    result = cursor.fetchall()
    if listar_produtos:
        print("Para voltar ao menu pressione \"q\"")
        for row in result:
            print(row)
        while True:
            if keyboard.is_pressed("q"):
                sleep(0.5)
                break
    return result
    