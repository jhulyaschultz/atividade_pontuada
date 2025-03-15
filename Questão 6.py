import os
os.system ("clear")

primeira_nota = float (input("digite a primeira nota:"))
segunda_nota = float (input("digite a segunda nota:")) 

media = ( primeira_nota + segunda_nota ) / 2

print  (f"media: (media)")
if media >= 6 :
    print ("parábens voce foi aprovado!")
else : 
    print ("reprovado!")
if media <= 4 :
    print ("reprovado!")