"""
Un camión puede transportar máximo 10,000 kg. Ingrese mercancías hasta
completar capacidad. Cada producto tiene:
Peso (kg)
•Tipo: Frágil ($2000/kg), Normal ($1000/kg), Peligroso ($5000/kg)
Reglas: No aceptar bultos > 1000 kg. 
Al final mostrar: total bultos, peso más liviano/pesado, 
ingresos, y distribución por tipo.
"""

#Ciclo para pedir bultos hasta completar 10000kgs
#pedir datos del bulto (peso y tipo)
#validar peso
#validar tipo
#sumar cantidad de bultos
#calcular el valor a pagar
#sumar valor 
#sumar cantidad de bultos fragil, cantidad de bultos normal 
#y cantidad de bultos peligrosos
#guardar el mayor valor
#guardar el menor valor

capacidad_camion=1000
peso_bulto=0
suma_peso_bultos=0
while suma_peso_bultos<capacidad_camion:
    peso_bulto=int(input("Ingrese peso bulto: "))
    if peso_bulto>1000:
        print("El peso del bulto excede máximo (1000). Intente de nuevo.")
        continue
    #fin del if
    suma_peso_bultos += peso_bulto
    tipo_bulto=input("Ingrese tipo (Frágil/Normal/Peligroso)").lower()
    if tipo_bulto not in ["frágil","normal","peligroso"]:
        print("Ingrese un tipo válido")
        continue


