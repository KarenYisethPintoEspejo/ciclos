#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:

numero = int(input("Introduzca un numero: "))
sum = 0
for i in range(numero):
    sum+=(-1)**(i)*(1/(2*i+1))
pi = 4 * sum
print(pi)