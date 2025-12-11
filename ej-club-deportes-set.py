deportes={"fútbol","natación","tenis"}

for deporte in deportes:
    print(deporte)

print("El club tiene ", len(deportes), " deportes")

#Pide al usuario un deporte 
# y verifica si ya se practica en el club
nuevo_deporte=input("Ingrese un nuevo deporte: ")
if nuevo_deporte in deportes:
    print("Ese deporte ya está en el club")
else:
    print("Ese deporte NO está en el club")

#Permite agregar un nuevo deporte al conjunto
nuevo_deporte=input("Agregue un nuevo deporte: ")
deportes.add(nuevo_deporte)
for deporte in deportes:
    print(deporte)

#Permite eliminar un deporte del conjunto
nuevo_deporte=input("Elimine un deporte: ")
if nuevo_deporte in deportes:
    deportes.discard(nuevo_deporte)
    print("El deporte ha sido eliminado")
else:
    print("Ese deporte NO está en el club")

for deporte in deportes:
    print(deporte)