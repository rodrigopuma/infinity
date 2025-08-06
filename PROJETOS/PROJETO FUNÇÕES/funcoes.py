from time import sleep
from tarefa import carregar_tarefas, salvar_tarefas_json

def validador_resposta(choice, *opcoes_validas):
    """Valida se a entrada do usuário está entre as opções válidas.

    Args:
        choice (any): A escolha do usuario
        *opcoes_validas (args/tuple): Todas as opções válidas passadas na hora da função

    Returns:
        any: Retorna a escolha válida para o programa
    """
    # Converte o valor para o tipo do primeiro argumento, se for diferente.
    # Evita erros de tipo entre string e int.
    try:
        choice = type(opcoes_validas[0])(choice)
    except (ValueError, IndexError):
        pass # Ignora a conversão se não for possível.

    # Loop para garantir que a escolha seja válida.
    while choice not in opcoes_validas:
        print(f'Escolha inválida. Opções válidas: {opcoes_validas}')
        choice = input('Selecione: ')
        # Tenta converter novamente para o tipo correto.
        try:
            choice = type(opcoes_validas[0])(choice)
        except ValueError:
            pass

    return choice

def menu():
    """Exibe o menu de opções e retorna a escolha do usuário."""
    print("""\033[1;31mMenu de Tarefas\033[m
    [0] - Criar Tarefa
    [1] - Ver todas as Tarefas
    [2] - Marcar Tarefa como concluída
    [3] - Remover Tarefa
    [4] - Filtrar por prioridade
    [5] - Filtrar por categoria
    [6] - Atualizar Tarefa""")
    
    # Solicitamos a entrada e validamos imediatamente.
    choice = input('Qual opção você deseja: ')
    return validador_resposta(choice, 0, 1, 2, 3, 4, 5, 6)

def renovar_ids(lista_tarefas: list):
    """Atualiza o 'ID' de cada tarefa na lista."""
    # Usa enumerate para atribuir IDs de 1 em diante.
    for indice, tarefa in enumerate(lista_tarefas, start=1):
        tarefa['ID'] = indice

def listar_tarefas(): 
    """Lista todas as tarefas de forma formatada."""
    # Carrega a lista de tarefas.
    lista_tarefas = carregar_tarefas()
    # Atualiza os IDs para garantir que estejam corretos antes de exibir.
    renovar_ids(lista_tarefas)
    
    # Se a lista estiver vazia, exibe uma mensagem.
    if not lista_tarefas:
        print('Nenhuma tarefa encontrada.')
        return

    for tarefa in lista_tarefas:
        sleep(0.3)
        print(f"""
-----------------------
ID: {tarefa['ID']}
Nome: {tarefa['nome']}
Descrição: {tarefa['descrição']}
Categoria: {tarefa['categoria']}
Prioridade: {tarefa['prioridade']}
Status: {'Concluído' if tarefa.get('status concluido', False) else 'Pendente'}
""")
        
def criar_tarefa():
    """Solicita os dados da tarefa e a adiciona ao arquivo JSON."""
    # Carrega as tarefas existentes
    lista_tarefas = carregar_tarefas()

    nome = input('\nDigite o nome: ')
    descricao = input('\nDigite a descrição: ')

    prioridade = input('\nDigite a prioridade (alta/media/baixa): ').lower().strip().replace('média', 'media')
    prioridade = validador_resposta(prioridade, 'alta', 'media', 'baixa')

    categoria = input('\nSelecione a categoria: ').lower().strip()

    nova_tarefa = {
        'nome': nome,
        'descrição': descricao,
        'categoria': categoria,
        'prioridade': prioridade,
        'status concluido': False
    }

    lista_tarefas.append(nova_tarefa)
    renovar_ids(lista_tarefas)
    salvar_tarefas_json(lista_tarefas)
    
    print('\nTarefa adicionada com sucesso!')

def solicitar_id(mensagem: str):
    """Função para solicitar e validar um ID numérico."""
    while True:
        try:
            # Tenta converter a entrada do usuário para um número inteiro.
            return int(input(mensagem))
        except ValueError:
            # Se a conversão falhar, informa o erro e repete o loop.
            print('Digite um número válido.')

def encontrar_tarefa_por_id(lista: list, id_tarefa: int):
    """Função auxiliar para encontrar uma tarefa pelo ID."""
    # Usa uma list comprehension para buscar a tarefa mais rapidamente.
    tarefa_encontrada = [t for t in lista if t.get('ID') == id_tarefa]
    # Retorna a tarefa se encontrada, ou None caso contrário.
    return tarefa_encontrada[0] if tarefa_encontrada else None

def remover_tarefa(lista: list):
    """Remove uma tarefa da lista pelo seu ID."""
    renovar_ids(lista)
    id_prompt = solicitar_id('Qual tarefa você deseja excluir? (Pelo ID, se não quiser digite 0): ')
    
    if id_prompt != 0:
        tarefa_a_remover = encontrar_tarefa_por_id(lista, id_prompt)
        if tarefa_a_remover:
            lista.remove(tarefa_a_remover)
            print('Tarefa removida com sucesso.')
            renovar_ids(lista) # Renova os IDs após a remoção.
        else:
            print('ID não encontrado.')
    else:
        print('Ok! Voltando ao menu inicial.')

def marcar_tarefa_concluida(lista: list):
    """Marca uma tarefa como concluída pelo seu ID."""
    renovar_ids(lista)
    id_prompt = solicitar_id('Qual tarefa você deseja concluir? (Pelo ID, se não quiser digite 0): ')
    
    if id_prompt != 0:
        tarefa_a_marcar = encontrar_tarefa_por_id(lista, id_prompt)
        if tarefa_a_marcar:
            tarefa_a_marcar['status concluido'] = True
            print('Tarefa marcada como concluída.')
        else:
            print('ID não encontrado.')
    else:
        print('Ok! Voltando ao menu inicial.')

def atualizar_tarefa(lista: list):
    """Atualiza as informações de uma tarefa pelo seu ID."""
    renovar_ids(lista)
    id_prompt = solicitar_id('Qual tarefa você deseja alterar? (Pelo ID, se não quiser digite 0): ')
    
    if id_prompt != 0:
        tarefa_a_atualizar = encontrar_tarefa_por_id(lista, id_prompt)
        
        if tarefa_a_atualizar:
            for chave, valor in tarefa_a_atualizar.items():
                # Evita que o usuário altere o ID.
                if chave == 'ID':
                    continue
                
                novo_valor = input(f'{chave}: {valor} (valor atual) -> Insira o novo valor (Enter para manter): ')
                
                if novo_valor:
                    # Converte o valor para o tipo original se for booleano
                    if isinstance(valor, bool):
                        tarefa_a_atualizar[chave] = novo_valor.lower() == 'true'
                    else:
                        tarefa_a_atualizar[chave] = novo_valor

            print('\nTarefa atualizada com sucesso!')
            percorrer_tarefa(tarefa_a_atualizar)
        else:
            print('ID não encontrado.')
    else:
        print('Ok! Voltando ao menu inicial.')

def exibir_tarefas_prioridade(lista: list):
    """Exibe as tarefas de uma prioridade específica."""
    prioridade = input('Qual prioridade (alta/media/baixa): ').lower().strip().replace('média', 'media')
    prioridade = validador_resposta(prioridade, 'alta', 'media', 'baixa')
    
    # Usa uma list comprehension para criar uma lista de tarefas filtradas.
    tarefas_filtradas = [t for t in lista if t.get('prioridade') == prioridade]
    
    if not tarefas_filtradas:
        print(f'Nenhuma tarefa com prioridade "{prioridade}" encontrada.')
    else:
        for tarefa in tarefas_filtradas:
            print(f"""
-----------------------
ID: {tarefa.get('ID')}
Nome: {tarefa.get('nome')}
Descrição: {tarefa.get('descrição')}
Categoria: {tarefa.get('categoria')}
Prioridade: {tarefa.get('prioridade')}
Status: {'Concluído' if tarefa.get('status concluido') else 'Pendente'}
""")

def exibir_tarefas_categoria(lista: list, categoria: str):
    """Exibe as tarefas de uma categoria específica."""
    # Usa uma list comprehension para criar uma lista de tarefas filtradas.
    tarefas_filtradas = [t for t in lista if t.get('categoria') == categoria]
    
    if not tarefas_filtradas:
        print(f'Nenhuma tarefa na categoria "{categoria}" encontrada.')
    else:
        for tarefa in tarefas_filtradas:
            print(f"""
-----------------------
ID: {tarefa.get('ID')}
Nome: {tarefa.get('nome')}
Descrição: {tarefa.get('descrição')}
Categoria: {tarefa.get('categoria')}
Prioridade: {tarefa.get('prioridade')}
Status: {'Concluído' if tarefa.get('status concluido') else 'Pendente'}
""")
            
def percorrer_tarefa(tarefa: dict):
    """Exibe os detalhes de uma única tarefa."""
    for chave, valor in tarefa.items():
        print(f'{chave}: {valor}')
        
# A função 'transformar_tarefas_lista' não é mais necessária,
# pois carregamos as tarefas diretamente onde precisamos.