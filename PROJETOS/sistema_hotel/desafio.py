"""Aplicativo de hotelaria

Crie uma classe Hotel que permita gerenciar
funcionários, reservas e quartos de hotel. Os
funcionários devem ter informações como nome,
função e salário. O hotel deve ser capaz de
receber reservas, atribuí-las a quartos e
calcular a conta final."""

from time import sleep
from classes import *
from tratamento import *
from functions import criar_funcionario, salvar, ler_arquivo, criar_reserva, adicionar_quarto
from arquivo import ARQUIVO_FUNCIONARIOS as ARQ_FUNC, ARQUIVO_QUARTOS as ARQ_QUART, ARQUIVO_RESERVAS as ARQ_RESER

lista_quartos = ler_arquivo(ARQ_QUART)

# print('Digite o número do quarto que deseja'), sleep(0.5)
# print('Opções: '), sleep(0.5)
# print('=' * 50)
# for quart in lista_quartos:
#     print(f'Número do quarto: {quart['n_quarto']}\nValor da Diária: R${f'{quart['valor_dia']:.2f}'.replace('.',',')}')
#     print('=' * 50)
# numero_quarto = input('Selecione: ').strip()

# for quarto in lista_quartos:
#     if quarto["n_quarto"] == numero_quarto:
#         reserva = criar_reserva(quarto)

# salvar(reserva, ARQ_RESER)

quarto = escolher_quarto()
reserva = criar_reserva(quarto) # Tem data
salvar(reserva, ARQ_RESER)
