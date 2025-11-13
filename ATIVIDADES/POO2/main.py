from desafio import ContaCorrente, ContaPoupanca, resumo

lrpl = ContaCorrente(312313, "Luiz Rodrigo Puma Lima", 50.00, 30000.20)

maassccb = ContaPoupanca(430520, "Maria Alice Sophia da Silva Costa Carneiro Barbosa", 20000.00)

lrpl.depositar(1000)
lrpl.sacar(2000)
lrpl.exibir_saldo()

print('='*100)

maassccb.exibir_saldo()
maassccb.calcular_juros()
maassccb.aumentar_juros(0.1)
maassccb.exibir_saldo()
maassccb.calcular_juros()
maassccb.exibir_saldo()

print('='*100)

resumo(lrpl)
print('='*100)
resumo(maassccb)
print('='*100)
lrpl.sacar(4000)
print('='*100)
resumo(lrpl)
