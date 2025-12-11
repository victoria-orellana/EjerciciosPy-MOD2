#Adivina número random con pistas de
#mayor o menor hast a acertar

import random
numero_secreto=random.randint(1,25)
adivina =0

print("Juguemos, adivina un numero entre 1 y 25")

while adivina != numero_secreto:
    adivina=int(input("Ingresa tu intento:"))

    if adivina < numero_secreto:
        print("ups mas arriba ")

    elif adivina > numero_secreto:
        print("ups mas abajo el numero")
    
    else : 
        print("jejej has adiviando pequeñx pitonizx")