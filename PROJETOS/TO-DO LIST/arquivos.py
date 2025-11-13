import json

def save_works(work: dict, path='lista_tarefa.json'):
    # 1️⃣ Tenta carregar as tarefas existentes
    works = load_works()
    print(f'Tarefas Existentes: \n{works}')

    # 2️⃣ Adiciona a nova tarefa à lista
    works.extend(work)

    # 3️⃣ Salva a lista completa no archive
    with open(path, 'w', encoding='utf-8') as archive:
        json.dump(works, archive, ensure_ascii=False, indent=4)

def load_works(path='lista_tarefa.json'):
    try:
        with open(path, 'r', encoding='utf-8') as archive:
            tarefas_carregadas = json.load(archive)
            return tarefas_carregadas
    except FileNotFoundError:
        return []
    
def add_list_for_json(new_list, path='lista_tarefa.json'):
    try:
        # Tenta carregar o conteúdo existente
        with open(path, 'r', encoding='utf-8') as archive:
            works_list = json.load(archive)
    except FileNotFoundError:
        # Se o archive não existir, começa com uma lista vazia
        works_list = []

    # Adiciona a nova lista (como um item inteiro ou adiciona os itens individualmente)
    works_list.extend(new_list)  # Para adicionar item por item
    # works_list.append(nova_lista)  # Para adicionar a lista inteira como um único item

    # Salva novamente no archive
    with open(path, 'w', encoding='utf-8') as archive:
        json.dump(works_list, archive, ensure_ascii=False, indent=4)

# Exemplo de uso
test_list = []
add_list_for_json(test_list)