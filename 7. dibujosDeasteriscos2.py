#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:

altura = int(input("Introduzca la altura del triangulo: "))

for i in range (altura):
    for j in range(i+1):
        print("*", end= " ")
    print()