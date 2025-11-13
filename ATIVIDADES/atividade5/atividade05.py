"""Crie uma classe chamada Fatura , a classe Fatura deve incluir
os seguintes atributos o nome do item; o preço unitário do item;
quantidade de item a ser faturado; valor total da fatura; Sua
classe deve ter um construtor que inicialize todos os atributos
menos o valor total da fatura. Forneça um método chamado
gerar_fatura que calcula o valor da fatura (isto é, multiplicar a
quantidade pelo preço por item)."""

class Fatura:
    def __init__(self, nome_item: str, preco_item: float, quantidade=1):
        self.item = nome_item
        self.preco = preco_item
        self.qtd = quantidade
    
    def gerar_fatura(self):
        self.valor_total = float(self.preco * self.qtd)
        print(f'O valor total foi de R${f'{self.valor_total:.2f}'.replace('.',',')}')
        return self.valor_total
    
fatura01 = Fatura('Computador', 1500, 20)
print(fatura01.gerar_fatura())
