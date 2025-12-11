#pide números al usuario y los suma
#termina cuando el usuario ingresa 0

#crea variable de suma
suma_de_numeros=0
num=int(input("Ingrese número: "))
#ciclo while mientras num distinto de cero
while num!=0:
    suma_de_numeros += num
    #pide num al usuario
    num=int(input("Ingrese número: "))
    #sumamos numeros
    

#termina el ciclo y mostramos la suma
print("La suma es:",suma_de_numeros)

