from tarefas import *
from arquivos import salvar_tarefas, carregar_tarefas

# Estrutura de dados
lista_tarefas = []

while True:
    choice = menu()
    # (FAZER) Renovação da lista - Do json para Python

    if choice == '0':
        tarefa = criar_tarefa()
        salvar_tarefas(tarefa)

    if choice == '1':
        lista_tarefas = carregar_tarefas()
        listar_tarefas(lista_tarefas)

    if choice == '2':
        listar_tarefas(lista_tarefas)
        marcar_tarefa_concluida(lista_tarefas)

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

