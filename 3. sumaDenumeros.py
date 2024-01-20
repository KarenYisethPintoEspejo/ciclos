#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. 
#Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.

numero1 = int(input("Introduzca un numero: "))
numero2 = int(input("Introduzca un numero: "))
sum = 0

for i in range (numero1+1,numero2):
    sum += i
print(f"La suma es de {sum}")