#Cuenta las consonantes de una palabra ingresada por el usuario

contador_de_consonantes=0
#pedir al usuario que ingrese
palabra = input("Ingrese una palabra: ")
#recorrer la palabra letra por letra
for letra in palabra:
#preguntar si es consonante/vocal
    if letra not in "aeiouAEIOU":
    #si es consonante, sumar 1 a variable contador
        contador_de_consonantes += 1
#imprimir cuántas consonantes son
print("La cantidad de consonantes es:",contador_de_consonantes)