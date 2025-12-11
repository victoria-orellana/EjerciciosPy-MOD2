"""
Muestra todos los estudiantes y sus notas.
2.Permite buscar la nota de un estudiante específico.
3.Permite agregar un nuevo estudiante con su nota.
4.Calcula y muestra el promedio de todas las notas
0. Salir
"""
estudiantes=dict()
#estudiantes={"juan":6.5, "luis":5} 
#estudiantes=dict("juan"=6.5, "luis"=5.0)

opcion=0
while True:
    print("1. Muestra todos los estudiantes")
    print("2. Buscar la nota de un estudiante")
    print("3. Agrega nuevo estudiante")
    print("4.Calcula y muestra el promedio")
    print("0. Salir")
    opcion=int(input("Ingrese opción: "))
    if opcion==0:
        break
    elif opcion==1:
        for x,y in estudiantes.items():
            print(x,y)
    elif opcion==2:
        nombre=input("Ingrese estudiante: ")
        print(estudiantes.get(nombre,"No existe"))
    elif opcion==3:
        nombre=input("Ingrese estudiante: ")
        nota=int(input("Ingrese nota: "))
        estudiantes[nombre]=nota
    elif opcion==4:
        suma=0
        for nota in estudiantes.values():
            suma+=nota
        print("Promedio", suma/len(estudiantes))