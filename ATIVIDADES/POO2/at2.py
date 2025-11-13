"""ATIVIDADE PRÁTICA 2

Crie uma hierarquia de classes que represente veículos. Comece com uma classe base "Veículo" e,
em seguida, crie classes derivadas como "Carro " e "Bicicleta." Adicione métodos para definir
atributos, como "cor" e "modelo," e permita a chamada de métodos em cadeia para configurar esses atributos."""

class Veiculo:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

class Carro(Veiculo):
    def __init__(self, cor, modelo):
        super().__init__(cor, modelo)
    
    def definir_cor(self, cor="Padrão"):
        if cor == "Padrão":
            pass
        else:
            super().cor = input('Digite a cor: ')
            