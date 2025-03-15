import os
os.system("clear")

renda_mensal = float(input("digite sua renda mensal: "))
valor_emprestimo = float(input("digite o valor total do emprestimo: "))
num_prestações = int(input("digite o numero de prestações: "))

prestação_mensal = valor_emprestimo / num_prestações

if valor_emprestimo <= 10 * renda_mensal and prestação_mensal <= 0.3 * renda_mensal:
    print("empréstimo APROVADO!!! ")
else:
    print("empréstimo NEGADO!!! ")