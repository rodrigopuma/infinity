
def main_menu():
    return int(input(f"""
{"Menu CRUD":^50}

1- Produto
2- Vendas

Selecione a opção desejada: """))

def menu_produto():
    return int(input(f"""
{"Menu Produto":^50}

1- Criar Produto
2- Listar Produtos
3- Editar Produto
4- Remover Produto
5- Voltar ao menu inicial

Selecione a opção desejada: """))

def menu_venda():
    return int(input(f"""
{"Menu Venda":^50}

1- Realizar Venda
2- Listar Vendas
3- Editar Venda
4- Remover Venda
5- Voltar ao menu inicial

Selecione a opção desejada: """))