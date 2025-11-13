"""ATIVIDADE PRÁTICA 3

Crie uma classe chamada "Calculadora" com um método "somar" que pode somar dois números inteiros
ou duas strings. Use o polimorfismo para implementar a sobrecarga do método " somar " para que ele
funcione com diferentes tipos de entrada (números inteiros e strings). 
Crie exemplos de uso para demonstrar como a mesma função pode se comportar de maneira 
diferente com base nos tipos de entrada."""

class Calculadora:
    def __init__(self, *args):
        self.args = args
    
    def somar(self):
        try:
            return sum(self.args)
        except TypeError:
            k = str()
            for i in self.args:
                if type(i) is int or type(i) is float:
                    i = str(i)
                k += i
            return k
    
calc1 = Calculadora('oi', 'mundo', 'tudo bem', 2, True)
print(calc1.somar())