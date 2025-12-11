#Recorre una palabra e imprime las vocales, 
#pero si encuentras la letra "z", termina.

#crear la palabra
palabra="ZOOLOGICO"
#recorrer la palabra letra por letra
for letra in palabra:
    #preguntar si es vocal
    if letra in "aeiouAEIOU":
    #si es vocal, imprimir
        print("Es vocal:" , letra)
    else:
    #si no es vocal, preguntamos si es z
        if letra=="z" or letra=="Z":
        #si es z se sale
            break
        #si no es z continua