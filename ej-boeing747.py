#ciclo mientras peso total sea menor a 3000 (para no ingresar tantos)
#validar que el bulto pese <500
#definir los rangos 0-25, 26-300, 301-500
#calculamos el valor a pagar

#numero total de bultos
#peso del bulto mas pesado y 
# del mas liviano
#peso promedio de los bultos

capacidad_carga=2000
peso_total=0
peso_bulto=0
numero_total_bultos=0
bulto_mas_pesado=0
bulto_mas_liviano=500
valor_total=0
valor_dolar=985
while peso_total < capacidad_carga:
    peso_bulto=int(input("Ingrese peso del bulto: "))
    if peso_bulto > 500:
        print("El peso del bulto excede máximo. Intente de nuevo.")
        continue
    peso_total += peso_bulto
    #numero total de bultos
    numero_total_bultos += 1
    if peso_bulto <= 25:
        valor = 0        
    elif peso_bulto <= 300:
        valor = peso_bulto * 1500
    else:
        valor = peso_bulto * 2500
    print("Valor a pagar ",valor)
    valor_total+=valor
    print("Carga acummulada: ", peso_total)

#peso del bulto mas pesado
    if peso_bulto > bulto_mas_pesado:
        bulto_mas_pesado = peso_bulto
# del mas liviano
    if peso_bulto < bulto_mas_liviano:
        bulto_mas_liviano = peso_bulto


#peso promedio de los bultos
peso_promedio=peso_total/numero_total_bultos

#valor en US$
valor_total_dolar=valor_total/valor_dolar

print("====== REPORTE DE BULTOS BOEING 747 ======")
print("Número total de bultos ingresados para el vuelo: ",numero_total_bultos)
print("Peso del bulto mas pesado: ",bulto_mas_pesado)
print("Peso del bulto mas liviano: ",bulto_mas_liviano)
print("Peso promedio de los bultos: ",peso_promedio)
print("Valor total de la carga en CLP$: ",valor_total)
print("Valor total de la carga en US$: ",valor_total_dolar)
