import json

PATH_ARQUIVO = 'tarefas.json'

def carregar_tarefas(path=PATH_ARQUIVO):
    """
    Carrega a lista de tarefas do arquivo JSON.
    Se o arquivo não existir, retorna uma lista vazia.
    """
    try:
        # Abre o arquivo no modo de leitura ('r') com a codificação correta.
        with open(path, 'r', encoding='utf-8') as archive:
            # Carrega o conteúdo JSON para uma lista Python.
            return json.load(archive)
    except FileNotFoundError:
        # Se o arquivo não for encontrado, retorna uma lista vazia.
        return []

def salvar_tarefas_json(lista_tarefas, path=PATH_ARQUIVO): # Unificando funções
    """
    Salva uma lista completa de tarefas no arquivo JSON.
    Esta função sobrescreve o conteúdo existente com a nova lista.
    """
    with open(path, 'w', encoding='utf-8') as archive:
        # Salva a lista de tarefas no arquivo JSON.
        # "ensure_ascii=False" permite caracteres especiais, e "indent=4" formata o arquivo.
        json.dump(lista_tarefas, archive, ensure_ascii=False, indent=4)