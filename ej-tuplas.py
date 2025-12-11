"""
Ejercicio 1: Días de la Semana (Inmutables)
Crea un programa que trabaje con una tupla de días 
de la semana  hábiles (lunes, martes, miércoles, jueves, viernes).

1. Muestra la tupla completa.
2. Pide al usuario un número del 1 al 5 y muestra el día 
correspondiente usando índices.
3. Pide al usuario un día y cuenta cuántas letras 
tiene usando métodos de tupla y len().

Convierte la tupla a lista, permite agregar un día festivo, y convierte de nuevo a tupla.
Muestra la nueva tupla.
"""
#crear la tupla con los dias
#crear ciclo
#pedirle al usuario la opcion
#para opcion 1 print con ciclo for
#para opcion 2 pedir número al usuario(1 a 5)
# mostrar dia usando el indice (-1)
#para opcion 3 pedir número al usuario(1 a 5)
#mostrar dia usando el indice (-1) 
# y calcular el largo con función len()

semana=("Lunes","Martes","Miércoles","Jueves","Viernes")
opcion=""
while True:
    print("========MENU=========")
    print("1. Muestra la tupla completa")
    print("2. Ver un dia")
    print("3. Ver el largo de un dia")
    print("4. Agregar sábado y domingo")
    print("0. Salir")
    opcion=int(input("Ingrese opción: "))
    if opcion==0:
        break
    elif opcion==1:
        for dia in semana:
            print(dia)
    elif opcion==2:
        num_dia=int(input("Ingrese número de día (1-5): "))
        print(semana[num_dia -1])
    elif opcion==3:
        num_dia=int(input("Ingrese número de día (1-5): "))
        print("Dia: ",semana[num_dia -1]," largo: ",len(semana[num_dia -1]))
        #len(semana) ---> 5
        #len(semana[2]) ---> 9
    elif opcion==4:
        lista_semana=list(semana)
        lista_semana.append("Sábado")
        lista_semana.append("Domingo")
        semana=tuple(lista_semana)