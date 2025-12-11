#pide números hasta que ingresen 0
#cuenta los pares e impares

num=1
contador_pares=0
contador_impares=0
while num!=0:
    num=int(input("Ingrese número: "))
    if num==0:
        break
    if num%2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

print("La cantidad de pares es: ", contador_pares)
print("La cantidad de impares es: ", contador_impares)

