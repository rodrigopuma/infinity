import json

from funcoes import (
    adicionar_tarefa_lista, atualizar_tarefa, 
    criar_tarefa, exibir_tarefas_categoria,
    exibir_tarefas_prioridade, listar_tarefas, 
    marcar_tarefa_concluida, menu, percorrer_tarefa, 
    remover_tarefa, renovar_ids, solicitar_id, 
    transformar_tarefas_lista, validador_resposta
)
from tarefa import carregar_tarefas, salvar_lista_json, salvar_tarefas, PATH_ARQUIVO

# Cada tarefa pode incluir informações como nome, descrição, prioridade e categoria.

# Estrutura de dados
lista_tarefas = []

tarefa = {
    'nome': str,
    'descricao': str,
    'prioridade': str,
    'categoria': str,
    'concluido': False
}

while True:
    choice = menu()

    if choice == 0: criar_tarefa()
        
    elif choice == 1: listar_tarefas()
        
    elif choice == 2:
        lista = carregar_tarefas()
        marcar_tarefa_concluida(lista)
        salvar_lista_json(lista)
    elif choice == 3:
        lista = carregar_tarefas()
        remover_tarefa(lista)
        salvar_lista_json(lista)
    elif choice == 4:
        lista = carregar_tarefas()
        exibir_tarefas_prioridade(lista)
    elif choice == 5:
        lista = carregar_tarefas()
        categoria = input('Digite a categoria: ').lower()
        exibir_tarefas_categoria(lista, categoria)
    elif choice == 6:
        lista = carregar_tarefas()
        atualizar_tarefa(lista)
        salvar_lista_json(lista)

