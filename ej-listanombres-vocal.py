#Para una lista de nombres,
#contar los que empiezan con vocal

#crear lista de nombres
nombres=["Darwin","Javiera","Ana","Loreto","Luis","Isabel","Matias","Vicente"]
#inicializar contador
contador_de_vocales=0
#recorrer la lista de nombres
for nombre in nombres:
#seleccionar la primera letra de la palabra
    if nombre[0] in "aeiouAEIOU":
    #preguntar si la letra es vocal
        contador_de_vocales +=1
#si es vocal, incrementar el contador

print("La cantidad de nombres de la lista que empiezan con vocal son:",contador_de_vocales)