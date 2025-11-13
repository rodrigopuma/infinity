"""ATIVIDADE PRÁTICA 4

Crie uma interface chamada "Veículo" com métodos "acelerar" e "frear." 
Em seguida, crie classes concretas como "Carro " e "Bicicleta " que implementem a interface
"Veículo " e forneçam suas próprias implementações dos métodos " acelerar " e "frear." 
Demonstre como o polimorfismo pode ser usado para tratar diferentes tipos de veículos de maneira 
uniforme, chamando os métodos da interface."""

class Veiculo:
    def __init__(self):
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 1
    
    def frear(self):
        self.velocidade -= 1

class Carro(Veiculo):
    def __init__(self):
        super().__init__()

class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__()

bike = Bicicleta()
car = Carro()
for _ in range(10):
    bike.acelerar()

print(bike.velocidadea)