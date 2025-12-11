#ciclo for (cantidad de pasajeros)
#pedimos edad al usuario
#validamos que esté en un rango normal(-1,120)
#sumar edad
#calcular el valor a pagar para cada rango
#llevar un contador para cada rango
#acumular el valor a pagar en una variable
#mostrar en pantalla el valor a pagar
#contador de pasajeros

#mostrar promedio edades (suma edades / contador de pasajors)

cantidad_pasajeros=5
suma_edades=0
valor_a_pagar=0
suma_valor_a_pagar=0
rangos={ "niño":0,
        "joven":0,
        "adulto":0,
        "adulto mayor":0
}
for i in range(cantidad_pasajeros):
    edad=-1
    while edad<0 or edad>110:
        edad = int(input("Ingrese la edad del pasajero: "))
        if edad<0 or edad>110:
            print("Edad fuera de rango")

    suma_edades += edad   
    if edad <=5:
        valor_a_pagar=0
        rangos["niño"]+=1
    elif edad <=18:
        valor_a_pagar=500
        rangos["joven"]+=1
    elif edad<=60:
        valor_a_pagar=800 
        rangos["adulto"]+=1
    else:
        valor_a_pagar=400
        rangos["adulto mayor"]+=1
    print("El valor a pagar del pasajero es: ",valor_a_pagar)
    suma_valor_a_pagar+=valor_a_pagar
#aquí termina el for

promedio_edades=suma_edades/cantidad_pasajeros
print("====== REPORTE DEL BUS ======")
print("Cantidad de pasajeros: ", cantidad_pasajeros)
print("Recaudación total del bus: ", suma_valor_a_pagar)
print("Promedio de edad de los pasajeros",promedio_edades)

for x, y in rangos.items():
  print("Rango ",x, " Pasajeros: ", y) 