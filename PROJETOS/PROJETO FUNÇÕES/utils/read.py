from time import sleep
from utils.db import load_works
from utils.functions import validador_resposta

def listar_tarefas(lista: list): 
    lista = load_works()
    for tarefa in lista:
        sleep(0.3)
        print(f"""-----------------------
ID: {tarefa['ID']}
Nome: {tarefa['nome']}
Descrição: {tarefa['descrição']}
Categoria: {tarefa['categoria']}
Prioridade: {tarefa['prioridade']}
Status: {'Concluído' if tarefa['status concluido'] is True else 'Pendente'}
""")

def exibir_tarefas_prioridade(lista: list): # Modificar
    prioridade = input('Qual prioridade: ').lower()
    prioridade = validador_resposta(prioridade, 'alta', 'media', 'média', 'baixa')
    if 'média' == prioridade:
        prioridade = 'media'
    for tarefa in lista:
        if tarefa['prioridade'] == prioridade:
            print(f"""-----------------------
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
            print(f"""-----------------------
ID: {tarefa['ID']}
Nome: {tarefa['nome']}
Descrição: {tarefa['descrição']}
Categoria: {tarefa['categoria']}
Prioridade: {tarefa['prioridade']}
Status: {'Concluído' if tarefa['status concluido'] else 'Pendente'}
""")
        else:
            pass