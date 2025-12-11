import random

lista = []
for i in range(5):  # 5 números aleatorios
    numero = random.randint(1, 10)  # entre 1 y 10
    lista.append(numero)

print(lista)  # Ej: [3, 7, 2, 9, 5]

lista_compras = ["manzana", "pan", "leche", "pan", "manzana"]
print("Lista:", lista_compras)