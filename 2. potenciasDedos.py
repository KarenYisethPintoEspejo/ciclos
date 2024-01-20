#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:
numero = int(input("Introduzca un numero: "))
for i in range(numero+1):
    print(f"{2**(i)}")
