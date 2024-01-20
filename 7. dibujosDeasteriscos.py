#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

altura = int(input("Introduzca la altura del rectangulo: "))
ancho = int(input("Introduzca el ancho del rectangulo: "))

for i in range (altura):
    for j in range (ancho):
        print("*", end= " ")
    print()