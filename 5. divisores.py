#Escriba un programa que entregue todos los divisores del número entero ingresado:

numero = int(input("Introduzca un numero: "))
divisores = []
for i in range(1,int(numero**0.5)):
    if numero%i==0:
        divisores.append(i)
for divisor in reversed(divisores):
    divisores.append(numero/divisor)
print(divisores)