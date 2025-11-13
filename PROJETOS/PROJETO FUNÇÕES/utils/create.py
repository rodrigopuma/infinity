from utils.functions import gerador_id, validador_resposta

def criar_tarefa():
    index = gerador_id()
    nome = input('\nDigite o nome: ')
    descricao = input('\nDigite a descrição: ')

    prioridade = input('\nDigite a prioridade: ').replace("média", "media")
    prioridade = validador_resposta(prioridade, 'alta', 'media', 'baixa')

    categoria = input('\nSelecione a categoria: ') # Quero fazer uma listinha de categorias
            
    tarefa = {
        'ID': index,
        'nome': nome,
        'descrição': descricao,
        'categoria': categoria.lower(),
        'prioridade': prioridade.lower(),
        'status concluido': False
    }

    return tarefa