import os
os.system ("clear")

primeiro_numero = int (input("digite um numero:"))
operador = input("digite a operação que deseja(+-*/): ")
segundo_numero = int (input("digite um numero: "))

match operador:
    case"+":
        resultado = primeiro_numero + segundo_numero
    case"-":
        resultado = primeiro_numero - segundo_numero
    case"*":
        resultado = primeiro_numero * segundo_numero
    case"/":
        resultado = primeiro_numero / segundo_numero
    case"_":
        resultado = "opção inválida."

print(f"\nprimeiro número: {primeiro_numero}")
print(f"operação:{operador}")
print(f"segundo número:{segundo_numero}")
print(f"resultado:{resultado}")
