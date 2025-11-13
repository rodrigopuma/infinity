"""DESAFIO PRÁTICO

sistema de gerenciamento de contas bancárias em Python

Crie um sistema de gerenciamento de contas bancárias
em Python usando herança e polimorfismo. O sistema
deve incluir as seguintes classes:

-A classe base "Conta" deve ter atributos para o número da conta, o titular da conta e o saldo.

-Ela deve incluir métodos para depósitos, saques e exibição do saldo atual.



Classe ContaCorrente:
-A classe "ContaCorrente" herda de "Conta" e inclui
atributos específicos, como taxa de manutenção e
limite de cheque especial.

-Deve sobrescrever o método de saque para
considerar o limite de cheque especial, se
necessário.



Classe ContaPoupanca:
-A classe "ContaPoupanca" também herda de "Conta" e inclui 
atributos específicos, como taxa de juros.

-Ela deve ter um método para calcular e adicionar juros ao
saldo.

-Crie um método chamado resumo que pode ser chamado
em qualquer objeto de conta (ContaCorrente ou
ContaPoupanca).



Esse método resumo irá exibir um resumo das
informações da conta, incluindo o tipo de conta
(corrente ou poupança), o número da conta, o
titular da conta e o saldo atual.

Teste de Funcionalidade:

Crie um programa principal que demonstre o uso dessas
classes. Crie instâncias de contas correntes e poupanças,
realize depósitos, saques, adicione juros e chame o
método resumo para cada conta.
"""

import datetime

class Conta:
    def __init__(self, numero_conta: str, titular: str, saldo: float=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor: float):
        if valor > self.saldo:
            print(f'Olá {self.titular.split(" ")[0]}! Não será possivel realizar o saque pois você não tem saldo suficiente.')
        else:
            self.saldo -= valor

    def exibir_saldo(self):
        print(f'Olá {self.titular.split(" ")[0]}! O seu saldo atual é de R${self.saldo:.2f}')

class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular, taxa_manutencao, limite_cheque_especial, saldo = 0.0):
        super().__init__(numero_conta, titular, saldo)
        self.taxa_manutencao = taxa_manutencao
        self.limite_cheque_especial = limite_cheque_especial
        self.debitos = []

    def sacar(self, valor):
        dttime = datetime.datetime.today()
        if valor > self.saldo:
            if self.limite_cheque_especial >= valor:
                choice = input(f'Olá {self.titular.split(" ")[0]}! Não é possível realizar o saque com saldo pois o saldo é insuficiente. \nMas você possui crédito do cheque especial, deseja utilizar?\n[1- Sim] | [2- Não]: ')
                while choice not in ["1", "2", "sim", "Sim", "Nao", "nao", "Não", "não"]:
                    choice = input("Opção inválida digite apenas [1]=Sim | [2]=Não")
                if choice in ["1", "Sim", "sim"]:
                    self.debitos.append({"Informações": "Saque com Cheque Especial", "Data": dttime, "Valor": valor})
                    self.limite_cheque_especial -= valor
                else:
                    if 5 <= datetime.time.hour <= 12:
                        print(f'Ok tenha um bom dia {self.titular.split(" ")[0]}!')
                    elif 13 <= datetime.time.hour <= 17:
                        print(f'Ok tenha uma boa tarde {self.titular.split(" ")[0]}!')
                    else:
                        print(f'Ok tenha uma boa noite {self.titular.split(" ")[0]}!')

    def alterar_limite_cheque_especial(self, valor):
        self.limite_cheque_especial = valor

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, titular, saldo = 0, taxa_juros=0.05):
        super().__init__(numero_conta, titular, saldo)
        self.taxa_juros = taxa_juros

    def calcular_juros(self):
        self.saldo += self.saldo * self.taxa_juros

    def aumentar_juros(self, juros):
        self.taxa_juros = juros

    
        
def resumo(conta):
    print(f"""Resumo da conta:
Conta do Tipo: {conta.__class__.__name__}
Número da conta: {conta.numero_conta}
Titular: {conta.titular}
Saldo da conta: {conta.saldo}""")
    if type(conta) is ContaCorrente:
        if conta.debitos:
            print(f"Débitos: {[d for d in conta.debitos]}")