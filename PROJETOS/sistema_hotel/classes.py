from random import randint

class Funcionario:
    def __init__(self, nome: str, funcao: str, salario: float):
        self.id = id([nome, randint(1000, 9999)])
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

    def __str__(self):
        return f'ID: {self.id},\nNome: {self.nome},\nFunção: {self.funcao},\nSalário: R${f'{self.salario:.2f}'.replace('.',',')}'
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "funcao": self.funcao,
            "salario": self.salario
            }

class Quarto:
    def __init__(self, numero_quarto: str, diaria: float):
        if type(numero_quarto) is int:
            numero_quarto = str(numero_quarto)
        self.numero_quarto = numero_quarto
        self.diaria = diaria

    def __str__(self):
        return f'Nº Quarto: {self.numero_quarto},\nValor da Diária: R${f'{self.diaria:.2f}'.replace('.',',')}'

    def to_dict(self):
        return {
            "n_quarto": self.numero_quarto,
            "valor_dia": float(self.diaria)
        }

class Reserva:
    def __init__(self, quarto: Quarto, inicio:str, fim:str):
        self.quarto = quarto
        self.tempo = [inicio, fim]

    def __str__(self):
        return f'Quarto: {self.quarto}\nIntervalo de Tempo: {self.tempo}'

    def to_dict(self):
        return {
            "quarto": self.quarto.to_dict(),
            "data_inicio": self.tempo[0],
            "data_fim": self.tempo[1],
            "intervalo": self.tempo
        }

class Hotel:
    def __init__(self, funcionarios: list, reservas: list[dict], quartos: list):
        pass