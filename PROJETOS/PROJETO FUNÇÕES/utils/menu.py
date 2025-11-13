from utils.functions import validador_resposta

def menu():
    print("""\033[1;31mMenu de Tarefas\033[m
    [0] - Criar Tarefa
    [1] - Ver todas Tarefas
    [2] - Marcar Tarefa como concluída
    [3] - Remover Tarefa
    [4] - Filtrar por prioridade
    [5] - Filtrar por categoria
    [6] - Atualizar Tarefa""")
    choice = input('Qual opção você deseja: ') 
    return validador_resposta(choice, '0', '1', '2', '3', '4', '5', '6')