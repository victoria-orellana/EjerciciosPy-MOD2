#Pide edades hasta que ingresen -1
#al salir, muestra el promedio de las edades
edad=0
suma_edades=0
cantidad=0
while edad!=-1:
    suma_edades += edad
    cantidad += 1
    edad=int(input("Ingrese edad:"))
    while edad<-1 or edad>110:
        print("Edad fuera de rango")
        edad=int(input("Ingrese nuevamente edad:"))

cantidad-=1    
print("Se han ingresado ",cantidad," edades")
print("El promedio es: ", suma_edades/cantidad)
