#pide un numero al usuario y muestra su tabla de multiplicar
#termina con 0

num=1
while num!=0:
    num=int(input("Ingrese número: "))
    if num==0:
        break
    print("==== TABLA DE MULTIPLICAR DEL ",num," ====")
    for i in range(1,11): 
        print(f"{num} x {i} = {num*i}")