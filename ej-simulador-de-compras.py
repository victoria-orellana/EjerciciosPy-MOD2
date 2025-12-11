#Muestra un menu que permite agregar productos a un carrito 
# y va mostrando la suma hasta que elija "pagar"

#declarar menu de productos
#declara carrito vacio
#ciclo que termine cuando el usuario escribe "pagar"
#pedirle que ingrese producto
#agregar producto al carrito
#hacer la suma y mostrarla

productos = {
    "galletas": 990,
    "leche": 990,
    "pan": 2500,
    "carne": 10000
}
carrito=dict()
op=""
while op!="pagar":
    for x, y in productos.items():
        print(x, y)
    op=input("Ingrese producto o pagar: ")
    if op=="pagar":
        break
    if op in productos.keys(): 
        carrito[op]=productos.get(op)
    else:
        print("Ese producto no existe")
suma=0
if not carrito:
    print("Carrito vacío")
else:   
    for x in carrito.values():
        suma+=x

print("El total a pagar es: ", suma)