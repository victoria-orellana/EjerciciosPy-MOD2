#pide un numero al usuario y cuenta regesiva hasta 0

#pedir num a usuario
#ciclo mientas mayor que 0
#mostrar numero
#restarle 1 al num

#num=int(input("Ingrese número: "))
#while num>0:
#    print(num)
#    num -= 1

#versión mas completa que pide num al usuario una y otra vez
#hasta que ingresa 0
num=1
while num!=0:
    num=int(input("Ingrese número: "))
    otro_num=num
    while otro_num>0:
        print(otro_num)
        otro_num -= 1
