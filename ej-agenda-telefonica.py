#crear diccionario vacío
#ciclo que controle el menu
# 1. Agregar contactos (nombre/teléfono)
# 2.Buscar un contacto por nombre y mostrar su teléfono.
# 3.Permite eliminar un contacto existente por su nombre
# 4.Imprime todos los contactos
# 0. Salir

agenda_telefonica=dict()

while True:
    print("1.Agregar contactos (nombre/teléfono)")
    print("2.Buscar un contacto")
    print("3.Eliminar un contacto")
    print("4.Imprime todos los contactos")
    print("0. Salir")
    opcion=int(input("Ingrese opción: "))
    if opcion==0:
        break
    elif opcion==1:
        #agenda_telefonica["Juan"]=569456789123
        #{"Juan":569456789123}
        nombre=input("Ingrese nombre: ")
        num_telefono=int(input("Ingrese número"))
        agenda_telefonica[nombre]=num_telefono
    elif opcion==2:
        nombre=input("Ingrese nombre a buscar: ")
        print(agenda_telefonica.get(nombre,"Contacto no existe"))
    elif opcion==3:
        nombre=input("Ingrese nombre a eliminar: ")
        agenda_telefonica.pop(nombre,"Contacto no existe")
    elif opcion==4:
        for x, y in agenda_telefonica.items():
            print(x, y)
    
