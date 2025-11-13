from datetime import datetime
from src.models.product import Produto

class Sale:
    def __init__(self, sell_product_id: int, sale_amount: int, sale_date: int, sale_id: int=None):
        self.sale_id = sale_id
        self.sell_product_id = sell_product_id
        self.sale_amount = sale_amount
        self.sale_date = sale_date

def send_sell_to_db(venda, db, cursor):
    sql = "INSERT INTO Products (name, descricao, quantidade_disponivel, preco) VALUES (%s, %s, %s, %s)"


    