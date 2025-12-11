"""
number=0
for number in range(10):
    if number==5:
        break
        #print("5")
    print("El número es:" + str(number) )

print("Fuera de loop")

nums=[ 4, 6, 1, 3, 5, 9, 7]
for i in nums:
    print(i)
    if i==5:
        print("Encontrado")
        break
"""

#Encuentra el primer número par en una lista y detén la búsqueda.
"""
nums=[ 1, 3, 5,4, 9, 7]
for x in nums:
    if x % 2==0:
        break
    print(x)
"""

#Recorre una lista y suma los números, pero si encuentras un 0, termina el ciclo.
"""
nums=[ 1, 3, 5, 0, 4, 9, 7]
suma=0
for x in nums:
    if x==0:
        break
    suma += x
    print(suma)
"""

#Contador de positivos: Cuenta números positivos en una lista, 
# pero si encuentras un número mayor a 100, termina.
"""
nums=[ 1, 3, -5, -50, 4, 101, 7, -25]
contador_de_positivos=0
for x in nums:
    if x>0 and x<=100:
        contador_de_positivos += 1
        #contador_de_positivos = contador_de_positivos + 1
        print(contador_de_positivos)
    
    if x>100:
        break
"""

#Números consecutivos: Recorre una lista y si encuentras dos números iguales seguidos, 
# imprime "Repetido" y termina.

nums=[ 1, 3, 5, 5, 4, 101, 7, -25]
num_anterior=0
for x in nums:
    print(x)
    if x==num_anterior:
        print("Repetido")
        break
    num_anterior=x

