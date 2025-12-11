"""
Cree un programa para crear nuestra Playlist favorita.
Menú con opciones para que el usuario ingrese
1. Agregar nueva canción
2. Agregar canción al principio de la lista
3. Eliminar canción de la lista
4. Mostrar la lista
0. Terminar el programa

"""
#declarar variables
#incializar lista vacía
#ciclo de menu
#mostrar menu en pantalla
#pedir usuario que elija opcion
#si opcion es 0
#   terminar el programa
#Si opcion es 1
#   pedir canción
#   agregar con append()
#si opcion es 2
#   pedir cancion
#   agrgamos con insert(0,)
#si opcion es 3
#   pedir cancion
#   eliminamos con remove()
#si opcion es 4
#   imprimir con for

playlist=list()
cancion=""

while True:
    print("1. Agregar nueva canción")
    print("2. Agregar canción al principio de la lista")
    print("3. Eliminar canción de la lista")
    print("4. Mostrar la lista")
    print("0. Terminar el programa")
    opcion=int(input("Ingrese opción: "))
    if opcion==0:
        break
    elif opcion==1:
        playlist.append(input("Ingrese canción: "))
    elif opcion==2:
        cancion=input("Ingrese canción primera: ")
        playlist.insert(0, cancion)
    elif opcion==3:
        cancion=input("Ingrese canción a eliminar: ")
        playlist.remove(cancion)
    elif opcion==4:
        for cancion in playlist:
            print(cancion)

    


