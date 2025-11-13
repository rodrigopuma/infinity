from utils.__init__ import Produto, Sale, con, cursor
from datetime import datetime

def create_product():
    nome = input("Escreva o nome do produto: ")
    descricao = input("Escreva uma descrição para o produto: ")
    quantidade_disponivel = int(input("Qual a quantidade disponivel: "))
    preco = float(input("Quanto custa: R$").replace(",", "."))
    produto = Produto(nome, descricao, quantidade_disponivel, preco)
    sql = "INSERT INTO produtos (nome, descricao, quantidade_disponivel, preco) VALUES (%s, %s, %s, %s)"
    values = (nome, descricao, quantidade_disponivel, preco)
    cursor.execute(sql, values)
    con.commit()
    print(f"Produto {nome} no valor de R${preco} criado com sucesso!")
    return produto

def vender(produto: Produto):
    # selecionar produto
    id_produto_vendido = produto.id
    quantidade_vendida = int(input("What's sale amount?"))
    data_venda = datetime.today()
    sql = "INSERT INTO vendas (id_produto_vendido, quantidade_vendida, data_venda) VALUES (%s, %s, %s, %s)"
    values = (id_produto_vendido, quantidade_vendida, data_venda)
    cursor.execute(sql, values)
    con.commit()
    print("Venda realizada com sucesso")
    return Sale(id_produto_vendido, quantidade_vendida, data_venda)
