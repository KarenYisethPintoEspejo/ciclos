#Escriba un programa que muestre una tabla de multiplicar como la siguiente:

for i in range (1,11):
    for j in range (1,11):
        producto = str(i*j)
        if j == 10:
            prod = producto.rjust(3)
        else:
            prod = producto.rjust(2)
        print(prod, end= " ")
print ()