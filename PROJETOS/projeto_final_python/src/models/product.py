from src.models.databaseconnection import db_pysql

con = db_pysql.connect()
cursor = con

class Produto:
    def __init__(self, nome: str, descricao: str, quantidade_disponivel: int, preco: float, produto_id: int=None):
        self.produto_id = produto_id
        self.nome = nome
        self.descricao = descricao
        self.quantidade_disponivel = quantidade_disponivel
        self.preco = preco
    
    def to_tuple(self):
        return (self.produto_id, self.nome, self.descricao, self.quantidade_disponivel, self.preco)
    
    def edit(self):
        self.nome = input(f"Nome atual ({self.nome}), digite o nome novo: ")
        
    def __str__(self):
        return f"Id: {self.produto_id}, Nome: {self.nome}, Descrição: {self.descricao}, Quantidade Disponível: {self.quantidade_disponivel}, Preço: {self.preco}"

def create(nome: str, descricao: str, quantidade_disponivel: int, preco: float, connection, cursor):
    produto = Produto(nome, descricao, quantidade_disponivel, preco)
    sql = "INSERT INTO Products (nome, descricao, quantidade_disponivel, preco) VALUES (%s, %s, %s, %s)"
    values = (nome, descricao, quantidade_disponivel, preco)
    cursor.execute(sql, values)
    connection.commit()
    return produto
    
