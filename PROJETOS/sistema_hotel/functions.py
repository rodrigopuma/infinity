import json
from classes import Funcionario, Quarto, Reserva
from arquivo import ler_arquivo, escrever_arquivo

def criar_funcionario(nome: str=None, funcao:str=None, salario: float=None):
    if nome is None:
        nome = input("Digite o nome do funcionário: ")
    if funcao is None:
        funcao = input("Digite a função do funcionário: ")
    if salario is None:
        salario = float(input("Digite o salário do funcionário: "))

    return Funcionario(nome, funcao, salario) # Retorna o objeto funcionario

def adicionar_quarto(numero_quarto: str=None, valor_diaria:float=None):
    if numero_quarto is None:
        numero_quarto = input('Digite o número do quarto: ')
    if valor_diaria is None:
        valor_diaria = float(input('Digite o valor da diária desse quarto: '))

    return Quarto(numero_quarto, valor_diaria)

def criar_reserva(quarto_obj:Quarto, inicio: str=None, fim:str=None):
    if inicio is None:
        inicio = input('Digite a data de ínicio "DD/MM/AA" ou "DD MM AA": ')
    if fim is None:
        fim = input('Digite a data de fim "DD/MM/AA" ou "DD MM AA": ')

    return Reserva(quarto_obj, inicio, fim)

def salvar(obj, db):
    """Salva um obj como dicionario em seu database

    Args:
        obj (obj): _description_
        db (file): _description_
    """
    escrever_arquivo(db, obj.to_dict())
