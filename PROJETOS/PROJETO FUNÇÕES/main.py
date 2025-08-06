from funcoes import (
    atualizar_tarefa, criar_tarefa,
    exibir_tarefas_categoria, exibir_tarefas_prioridade,
    listar_tarefas, marcar_tarefa_concluida,
    menu, remover_tarefa
)
from tarefa import carregar_tarefas, salvar_tarefas_json

# --- Refatoração do código principal ---

# Vamos eliminar a repetição de carregar e salvar a lista.
# A função "criar_tarefa" já lida com o salvamento, então não precisamos mexer nela.
# Para os outros casos, podemos criar uma função auxiliar para lidar com a lógica.

def gerenciar_tarefas(funcao, *args):
    """Carrega as tarefas, executa uma função de manipulação e salva.

    Args:
        funcao (def): Função usada para o gerenciamento
    """
    # Carrega a lista de tarefas do arquivo JSON.
    lista_tarefas = carregar_tarefas()
    
    # Chama a função de manipulação (remover, marcar, atualizar, etc.).
    # Passamos a lista e outros argumentos que a função possa precisar.
    funcao(lista_tarefas, *args)
    
    # Salva a lista de tarefas atualizada no arquivo.
    salvar_tarefas_json(lista_tarefas)

# O loop principal mais limpo e conciso.
while True:
    choice = menu()

    # O "criar_tarefa()" já tem sua própria lógica de salvamento.
    if choice == 0:
        criar_tarefa()
    
    # "listar_tarefas()" e "exibir_tarefas..." apenas leem, não precisam salvar.
    elif choice == 1:
        listar_tarefas()
    
    elif choice == 2:
        listar_tarefas() # Para o usuario escolher a tarefa que deseja
        gerenciar_tarefas(marcar_tarefa_concluida)
    
    elif choice == 3:
        listar_tarefas() # Para o usuario escolher a tarefa que deseja
        gerenciar_tarefas(remover_tarefa)

    elif choice == 4:
        # A função de exibir por prioridade não modifica a lista, então não precisa salvar.
        lista = carregar_tarefas()
        exibir_tarefas_prioridade(lista)
    
    elif choice == 5:
        # Similar ao anterior, apenas exibe.
        lista = carregar_tarefas()
        categoria = input('Digite a categoria: ').lower()
        exibir_tarefas_categoria(lista, categoria)
    
    elif choice == 6:
        listar_tarefas() # Para o usuario escolher a tarefa que deseja
        gerenciar_tarefas(atualizar_tarefa)