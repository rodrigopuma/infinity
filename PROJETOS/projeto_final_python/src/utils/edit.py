from __init__ import con, cursor, Produto

def editar_item(obj):
    obj.edit()
    print(obj)
    values = obj.to_tuple()

produto = Produto("Rackel", "", 1, 1)

editar_item(produto)