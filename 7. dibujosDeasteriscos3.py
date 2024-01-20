#Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:

lado = int(input("Introduzca la longitud del lado: "))
hexfin = lado + 2*(lado-1)
for i in range(lado):
    hexfinst = " "
    for j in range(lado+2*i):
        hexfinst += "*"
    print(hexfinst.center(hexfin))
for x in range(1,lado):
    hexfinst=" "
    for j in range (2,lado+2*(lado-x),1):
        hexfinst+="*"
    print(hexfinst.center(hexfin))



    
