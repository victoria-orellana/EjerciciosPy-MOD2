grupo1 = [5,13,16,7] 
grupo2 = [5,14,15,20]

for numero1 in grupo1:
    for numero2 in grupo2:
        if numero1==numero2:
            continue
        elif numero1> numero2:
            break
        else:
            print("Conclusión ",numero1, "es menor que ",numero2)

#numero1 5 5  5  5  13
#numero2 5 14 15 20  5

"""
numeros_externos = [1, 2, 3]
numeros_internos = [10, 20, 30]

for ext in numeros_externos:          # Ciclo externo
    print(f"Externo: {ext}")

    for interno in numeros_internos:  # Ciclo interno
        print(f"   Interno: {interno}")

    print("--- fin del ciclo interno ---")
"""

numeros = [1,2,3]
letras = ['a','b','c']

for n1 in numeros:
    print(f'{n1}')
    for n2 in letras:
        print(n2)
        