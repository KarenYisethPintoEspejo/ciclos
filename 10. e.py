#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.

import math
denominador = 2
diferencia = 1
e = 2
fraccionpre = 1
fraccion = 1

while diferencia>0.0001:
    fraccionpre = fraccion
    fraccion = 1/math.factorial(denominador)
    denominador += 1
    e += fraccion
    diferencia = fraccionpre - fraccion
print(e)