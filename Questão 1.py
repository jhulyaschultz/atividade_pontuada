import os
os.system ("clear")

#faça um alogoritimo que leia oa valores a,b,c e imprima na tela se é maior ou menor que c

primeiro_numero = int(input("digite o primeiro numero: "))
segundo_numero =  int(input("digite o segundo numero: "))
terceiro_numero = int(input("digite o terceiro_numero: ")) 

soma =  primeiro_numero + segundo_numero

if soma > terceiro_numero:
   print ("é maior que terceiro_numero.")
else :
   print ("é menor que terceiro_numero.")