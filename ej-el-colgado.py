#creamos variable con palabra secreta
#queso ***s* **es*
#pedirle al usuario que ingrese letras
#para cada letra decirle si está o no
#si ingresa una letra correcta, mostrar el avance
#el juego termina si el usario ingresa 0
#el juego termina cuando descubre la palabra

palabra_secreta="python"
palabra_oculta=["*","*","*","*","*","*"] #cómo le agregamos los *?

while palabra_secreta!=palabra_oculta:
    print("Adivina la palabra: ", palabra_oculta)
    letra = input("Ingresa una letra (0 para salir): ")
    if letra=="0":
        break
    if letra in palabra_secreta:
        print("Has encontrado una letra!")
        #palabra="python"
        #["p","y","t","h","o","n"]
        #[ 0 , 1 , 2 , 3 , 4 , 5 ]
        for i in range(len(palabra_secreta)):
            if letra == palabra_secreta[i]:
                palabra_oculta[i]=letra
    else:
        print("Esa letra no está")

