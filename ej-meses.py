#Crear tupla de meses del año
#hacer un ciclo
#pedirle números al usuario
#validar que estén entre 1 y 12
#si es cero terminar el programa
#imprimir el mes

meses=("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
mes_usuario=0

while mes_usuario>=0 and mes_usuario<=12:
    mes_usuario=13
    while mes_usuario<0 or mes_usuario>12:
        mes_usuario=int(input("Ingrese número del mes (0-termina): "))
        if mes_usuario<0 or mes_usuario>12:
            print("Ingrese un valor dentro del rango 1-12")
    
    if mes_usuario==0:
        break

    print("El mes que ha ingresado es:")
    print(meses[mes_usuario-1])