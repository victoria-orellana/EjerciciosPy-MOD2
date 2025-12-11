edades = [5,13,16,7]
edades.insert(7,21)

for edad in edades:
    print(edad)

lista=["Hola","mundo","mundo"]
print(lista.count("mundo"))

for x in lista:
    print(x)

otra_lista=[3,5,8,1,4,45,12,9]
print("Largo lista original: ", len(otra_lista))
for x in otra_lista:
    print(x)
del otra_lista[5]
print("Largo lista modificada: ", len(otra_lista))
for x in otra_lista:
    print(x)