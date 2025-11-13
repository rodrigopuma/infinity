from utils.create import criar_tarefa
from utils.delete import remover_tarefa
from utils.menu import menu
from utils.read import exibir_tarefas_categoria, exibir_tarefas_prioridade, listar_tarefas
from utils.update import marcar_tarefa_concluida, atualizar_tarefa
from utils.db import save_works

# Estrutura de dados
lista_tarefas = []

while True:
    choice = menu()
    # (FAZER) Renovação da lista - Do json para Python

    if choice == '0':
        tarefa = criar_tarefa()
        save_works(tarefa)

    if choice == '1':
        listar_tarefas()

    if choice == '2':
        listar_tarefas()
        marcar_tarefa_concluida()

    if choice == '3':
        listar_tarefas(lista_tarefas)
        remover_tarefa(lista_tarefas)

    if choice == '4':
        exibir_tarefas_prioridade(lista_tarefas)
    
    if choice == '5':
        categoria = input('Qual a categoria: ')
        exibir_tarefas_categoria(lista_tarefas, categoria)

    if choice == '6':
        atualizar_tarefa(lista_tarefas)

