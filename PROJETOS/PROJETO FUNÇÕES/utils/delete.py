from utils.functions import solicitar_id

def remover_tarefa(lista: list):
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