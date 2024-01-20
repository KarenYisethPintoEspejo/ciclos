#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
tiempoviaje = int(input("Introduzca la duracion del tramo: "))
tiempototal = 0
while tiempoviaje !=0:
    tiempototal+=tiempoviaje
    tiempoviaje = int(input("Introduzca la duracion del tramo: "))
print(f"El tiempo total del viaje es de: {tiempoviaje//60}:{str(tiempototal%60).zfill(2)} horas")
