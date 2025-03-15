import os
os.system ("clear")

#Uma fruteira está vendendo frutas com a seguinte tabela de preços.

kg_morango = float(input("digite a quantidade de morangos: "))
kg_maca = float(input("digite a quantidade de macas:"))
 
if kg_morango >  5:
    preco_morango = 2.20
else:
    preco_morango = 2.50
if kg_maca >5:
    preco_maca = 1.50
else:
    preco_maca = 1.80 

total_morango = kg_morango * preco_morango 
total_maca = kg_maca * preco_maca 
total_compra = total_morango + total_maca

if(kg_morango + kg_maca) >= 10 or total_compra >= 15:
   total_compra *= 0.90
print(f"valor a ser pago : R$ {total_compra : .2f}")
