import os
os.system("clear")


preco_alcool = 3.79
preco_gasolina = 6.59


litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ").upper()

if tipo_combustivel == 'A':
    if litros_vendidos <= 25:
        desconto = 0.02 
    else:
        desconto = 0.04  
    preco_com_desconto = preco_alcool * (1 - desconto)
    valor_pago = litros_vendidos * preco_com_desconto
    print(f"O valor a ser pago pelo cliente é R$ {valor_pago:.2f} (Álcool com desconto)")

elif tipo_combustivel == "G":
    if litros_vendidos <= 25:
        desconto = 0.03  
    else:
        desconto = 0.05  
    preco_com_desconto = preco_gasolina * (1 - desconto)
    valor_pago = litros_vendidos * preco_com_desconto
    print(f"O valor a ser pago pelo cliente é R$ {valor_pago:.2f} (Gasolina com desconto)")

else:
    print("Tipo de combustível inválido. Digite 'A' para Álcool ou 'G' para Gasolina.")