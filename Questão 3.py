import os
os.system ("clear")

#Faça um algoritmo que leia dois valores inteiros A e B.

primeiro_numero = int(input("digite o primeiro numero: "))
segundo_numero = int(input("digite o segundo numero: "))


if primeiro_numero == segundo_numero:
    soma = primeiro_numero + segundo_numero
    print("valor c:", soma)
else:
    multiplicação = primeiro_numero * segundo_numero
    print("valor c: ", multiplicação)
        