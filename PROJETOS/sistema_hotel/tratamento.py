from .arquivo import ler_arquivo, escrever_arquivo, ARQUIVO_FUNCIONARIOS as F, ARQUIVO_QUARTOS as Q, ARQUIVO_RESERVAS as R
from .classes import Quarto

lista_funcionarios = ler_arquivo(F)
lista_quartos = ler_arquivo(Q)
lista_reservas = ler_arquivo(R)

def escolher_quarto(lista:list=lista_quartos):
    print('Digite o número do quarto que deseja') 
    print('Opções: ')
    print('=' * 50)
    for quarto in lista_quartos:
        print(f'Número do quarto: {quarto['n_quarto']}\nValor da Diária: R${f'{quarto['valor_dia']:.2f}'.replace('.',',')}')
    print('=' * 50)
    numero_quarto = input('Selecione: ').strip()
    for quarto in lista_quartos:
        if quarto["n_quarto"] == numero_quarto:
            return Quarto(numero_quarto, quarto["valor_dia"])

    