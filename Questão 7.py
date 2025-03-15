import os
os.system("clear")

nome = input("digite o nome do produto: ")
quantidade = int(input("digite a quantidade adquirida: "))
preço_unitario =float(input("digite o preço unitário: "))

total = quantidade * preço_unitario

if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.02
else:
    desconto = total * 0.05     

total_a_pagar = total = desconto
print(f"produto: {nome}")       
print(f"total sem desconto: {total}")       
print(f"desconto aplicado: R$ {desconto}")       
print(f"tota a pagar: R$ {total_a_pagar}")




















