from time import sleep
from tarefa import carregar_tarefas, salvar_lista_json

def validador_resposta(choice, *args):
    while choice not in args:
        print(f'Escolha inválida. Opções válidas: {args}')
        choice = input('Selecione: ')
    return choice

def menu():
    print("""\033[1;31mMenu de Tarefas\033[m
    [0] - Criar Tarefa
    [1] - Ver todas Tarefas
    [2] - Marcar Tarefa como concluída
    [3] - Remover Tarefa
    [4] - Filtrar por prioridade
    [5] - Filtrar por categoria
    [6] - Atualizar Tarefa""")
    choice = int(input('Qual opção você deseja: ')) 
    choice = validador_resposta(choice, 0, 1, 2, 3, 4, 5, 6)
    return choice

def transformar_tarefas_lista():
    tarefas_json = carregar_tarefas()
    renovar_ids(tarefas_json)
    return tarefas_json

def criar_tarefa(lista=carregar_tarefas()):
    nome = input('\nDigite o nome: ')
    descricao = input('\nDigite a descrição: ')

    prioridade = input('\nDigite a prioridade (alta/media/baixa): ').lower().replace('média', 'media')
    prioridade = validador_resposta(prioridade, 'alta', 'media', 'baixa')

    categoria = input('\nSelecione a categoria: ')

    tarefa = {
        'ID': None,
        'nome': nome,
        'descrição': descricao,
        'categoria': categoria.lower(),
        'prioridade': prioridade.lower(),
        'status concluido': False
    }
    lista.append(tarefa)
    renovar_ids(lista)
    salvar_lista_json(lista)
    print('Tarefa adicionada com sucesso!')

    return tarefa


def renovar_ids(lista: list):
    for indice, tarefa in enumerate(lista, start=1):
        tarefa['ID'] = indice

def listar_tarefas(): 
    lista = transformar_tarefas_lista()
    for tarefa in lista:
        sleep(0.3)
        print(f"""
-----------------------
ID: {tarefa['ID']}
Nome: {tarefa['nome']}
Descrição: {tarefa['descrição']}
Categoria: {tarefa['categoria']}
Prioridade: {tarefa['prioridade']}
Status: {'Concluído' if tarefa['status concluido'] is True else 'Pendente'}
""")

def marcar_tarefa_concluida(lista: list): # Modificar
    renovar_ids(lista)
    index_prompt = solicitar_id('Qual tarefa você deseja concluir? (Pelo ID, se não quiser digite 0): ')
    if index_prompt != 0:
        for tarefa in lista:
            if tarefa['ID'] == index_prompt:
                tarefa['status concluido'] = True
                break
            else: pass
        else:
            print('Não foi encontrado nenhum ID para essa tarefa.')
    else:
        print('Ok! Voltando ao menu inicial.')

def exibir_tarefas_prioridade(lista: list): # Modificar
    prioridade = input('Qual prioridade: ').lower().strip().replace('média','media')
    prioridade = validador_resposta(prioridade, 'alta', 'media', 'baixa')

    for tarefa in lista:
        if tarefa['prioridade'] == prioridade:
            print(f"""
-----------------------
ID: {tarefa['ID']}
Nome: {tarefa['nome']}
Descrição: {tarefa['descrição']}
Categoria: {tarefa['categoria']}
Prioridade: {tarefa['prioridade']}
Status: {'Concluído' if tarefa['status concluido'] else 'Pendente'}
""")
        else:
            pass

def exibir_tarefas_categoria(lista: list, categoria: str): # Modificar
    for tarefa in lista:
        if tarefa['categoria'] == categoria:
            print(f"""
-----------------------
ID: {tarefa['ID']}
Nome: {tarefa['nome']}
Descrição: {tarefa['descrição']}
Categoria: {tarefa['categoria']}
Prioridade: {tarefa['prioridade']}
Status: {'Concluído' if tarefa['status concluido'] else 'Pendente'}
""")
        else:
            pass

def solicitar_id(mensagem: str):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Digite um número válido.')

def remover_tarefa(lista: list):
    renovar_ids(lista)
    index_prompt = solicitar_id('Qual tarefa você deseja excluir? (Pelo ID, se não quiser digite 0): ')
    if index_prompt != 0:
        for tarefa in lista:
            if tarefa['ID'] == index_prompt:
                lista.remove(tarefa)
                print('Tarefa removida com sucesso.')
                break
        else:
            print('ID não encontrado.')
    else:
        print('Ok! Voltando ao menu inicial.')

def percorrer_tarefa(tarefa=dict()):
    for chave, valor in tarefa.items():
        print(f'{chave}: {valor}')

def atualizar_tarefa(lista: list):
    renovar_ids(lista)
    index_prompt = solicitar_id('Qual tarefa você deseja alterar? (Pelo ID, se não quiser digite 0): ')
    if index_prompt != 0:
        for tarefa in lista:
            if tarefa['ID'] == index_prompt:
                for chave, valor in tarefa:
                    valor_antigo = valor
                    tarefa[chave] = input(f'{chave}: {valor} (valor atual) insira o valor que deseja colocar se não quiser alterar apenas pressione Enter: ')
                    if valor == '':
                        valor = valor_antigo
                print('Tarefa atualizada: ')
                percorrer_tarefa(tarefa)
                break
            
        else:
            print('ID não encontrado.') 
    else:
        print('Ok! Voltando ao menu inicial.')

# Teste
lista_tarefas = []
criar_tarefa()
criar_tarefa()
print(lista_tarefas)
salvar_lista_json(lista_tarefas)