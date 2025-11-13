"""ATIVIDADE PRÁTICA 1 
Crie uma hierarquia de classes representando formas geométricas. 
Comece com uma classe base chamada "Forma " e, em seguida, crie classes derivadas como 
"Círculo " e "Retângulo " que herdem da classe base. Adicione métodos para calcular área
e perímetro em cada classe derivada."""

class Forma:
    def __init__(self, medida):
        self.medida = medida

class Circulo(Forma):
    def __init__(self, medida):
        super().__init__(medida)
    
    def calcular_area(self):
        return 3.14 * self.medida ** 2
    
    def calcular_perimetro(self):
        return 2 * 3.14 * self.medida
    
class Retangulo(Forma):
    def __init__(self, medida, medida2):
        super().__init__(medida)
        self.medida2 = medida2

    def calcular_area(self):
        return self.medida * self.medida2
    
    def calcular_perimetro(self):
        return (self.medida * 2) + (self.medida2 * 2)

ret = Retangulo(2,5)
print(ret.calcular_area())
print(ret.calcular_perimetro())