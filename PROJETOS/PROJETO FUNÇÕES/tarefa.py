import json

PATH_ARQUIVO = 'tarefas.json'

# class Tarefa:
#     def __init__(self, nome, descricao, prioridade, categoria):
#         self.nome = nome
#         self.descricao = descricao
#         self.prioridade = prioridade
#         self.categoria = categoria

#         tarefa = {
#             'nome': self.nome,
#             'descricao': self.descricao,
#             'prioridade': self.prioridade,
#             'categoria': self.categoria
#         }

#         return tarefa
    

def salvar_tarefas(tarefa: dict, path=PATH_ARQUIVO):
    """_summary_

    Args:
        tarefa (dict): adiciona a tarefa que esta tentando salvar
        path (caminho_arquivo, optional): _description_. Defaults to PATH_ARQUIVO.

    Tenta carregar as tarefas existentes
    Adiciona a nova tarefa à lista
    Salva a lista completa no arquivo json
    """
    lista_tarefas = carregar_tarefas() 
    lista_tarefas.append(tarefa)
    with open(path, 'w', encoding='utf-8') as archive:
        json.dump(lista_tarefas, archive, ensure_ascii=False, indent=4)

def carregar_tarefas(path=PATH_ARQUIVO):
    try:
        with open(path, 'r', encoding='utf-8') as archive:
            tarefas_carregadas = json.load(archive)
            return tarefas_carregadas # Retorna uma lista de tarefas
    except FileNotFoundError:
        return []
    
def salvar_lista_json(nova_lista, path=PATH_ARQUIVO):
    try:
        # Tenta carregar o conteúdo existente
        with open(path, 'r', encoding='utf-8') as archive:
            lista_tarefas = json.load(archive)
    except FileNotFoundError:
        # Se o archive não existir, começa com uma lista vazia
        lista_tarefas = []

    # Adiciona a nova lista (como um item inteiro ou adiciona os itens individualmente)
    lista_tarefas.extend(nova_lista)  # Para adicionar item por item
    # lista_tarefas.append(nova_lista)  # Para adicionar a lista inteira como um único item

    # Salva novamente no archive
    with open(path, 'w', encoding='utf-8') as archive:
        json.dump(lista_tarefas, archive, ensure_ascii=False, indent=4)

# Teste
lista_teste = []
salvar_lista_json(lista_teste)