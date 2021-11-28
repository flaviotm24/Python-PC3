import os
def pedirnumero():
    a= int(input("Ingrese el valor de a: "))
    b= int(input("Ingrese el valor de b: "))
    os.system("cls")
    return a,b 

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def menu(a,b):
    while True:
        print(f"Que tipo de operacion matematica deseas realizar con {a} y {b}\n\
s para sumar\n\
r para restar\n\
m para multiplicar\n\
d para dividir\n\
x para salir:")
        opcion=input()
        if opcion== "s":
            print(f"Resultado es:{suma(a,b)}")
        if opcion== "r":
            print(f"Resultado es:{resta(a,b)}")
        if opcion== "m":
            print(f"Resultado es:{multiplicar(a,b)}")
        if opcion== "d":
            print(f"Resultado es:{dividir(a,b)}")
        elif opcion=="d"and b == 0:
            print ("ERROR Tipo de dato no valido") 
        if opcion == "x":
            break
        input ("Presione cualquier tecla")
        os.system("cls")
