from utils.functions import solicitar_id

def atualizar_tarefa(lista: list):
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
                for chave, valor in tarefa.items():
                    print(f'{chave}: {valor}')
                break
            
        else:
            print('ID não encontrado.')
    else:
        print('Ok! Voltando ao menu inicial.')

def marcar_tarefa_concluida(lista: list): # Modificar
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
