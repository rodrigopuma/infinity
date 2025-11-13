"""ATIVIDADE PRÁTICA 5

Crie uma classe base chamada "Animal" com um método " emitirSom." Em seguida, crie classes derivadas como "Cachorro, "
"Gato " e "Pássaro " que herdem de "Animal" e sobrescrevam o método " emitirSom "
para cada tipo de animal. Crie uma lista de animais e percorra-a, chamando o método " emitirSom "
para cada animal. Demonstre como o polimorfismo permite que diferentes tipos de animais emitam seus sons de
maneira uniforme."""

class Animal:
    def emitirSom(self):
        pass

class Cachorro(Animal):
    def emitirSom(self):
        return "Woof"
class Gato(Animal):
    def emitirSom(self):
        return "Miau"
class Passaro(Animal):
    def emitirSom(self):
        return "Piu Piu"
    
animais = [Cachorro(), Gato(), Passaro(), Gato(), Passaro()]

for animal in animais:
    print(f"{animal.__class__.__name__} faz {animal.emitirSom()}")