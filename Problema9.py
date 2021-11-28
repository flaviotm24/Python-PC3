import random

intentos_realizados= 0

print("¡Hola! ¿Como te llamas?")
minombre= input()

numero= random.randint(1,100)
print("Bueno, "+ minombre +", estoy pensando en un numero entre 1 y 100.")

while intentos_realizados < 6:
    print("Intenta adivinar.")
    estimacion= input()
    estimacion= int(estimacion)

    intentos_realizados = intentos_realizados + 1

    if estimacion < numero:
        print("Tu estimacion es muy baja.")
    if estimacion > numero:
        print ("Tu estimacion es muy alta.")
    if estimacion == numero:
        break
if estimacion == numero:
    intentos_realizados = str(intentos_realizados)
    print("¡Buen trabajo. "+ minombre +"! ¡Has adivinado mi numero en "+ intentos_realizados+" intentos!")

if estimacion != numero:
    numero = str(numero)
    print("Pues no. El numero que estaba pensando era"+ numero)
