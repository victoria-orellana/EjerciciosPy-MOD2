#crear un dictionario 
#preguntar cuántos clientes responderán la encuesta
#validar que número de clientes sea >0
#ciclo que se ejecute tantas veces como clientes haya (for)
#preguntar sandwich favorito
#incrementar la suma del sandwich elegido
#imprimir lista con las preferencias
#buscar el favorito e imprimirlo

menu={"Hamburguesa": 0,
        "Churrasco": 0,
        "Lomito": 0,
        "Completo": 0}

sandwich=""
cantidad_clientes=0

while cantidad_clientes<=0:
    cantidad_clientes=int(input("Ingrese cantidad de clientes: "))
    if cantidad_clientes==0:
        print("Ingrese un valor válido")

for i in range(cantidad_clientes):
    for x in menu.keys():
        print(x)
    sandwich=input("Ingrese sandwich favorito del cliente ")
    menu[sandwich] += 1

for x, y in menu.items():
  print(x, y)   

cantidad_mayor=0
sandwich_mayor=""
for x, cantidad in menu.items():
    if cantidad > cantidad_mayor:
        cantidad_mayor = cantidad
        sandwich_mayor=x

print("El sandwich favorito es: ",sandwich_mayor," con ",cantidad_mayor," de preferencias")