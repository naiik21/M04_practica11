"""
En esta funcion te pedira que le
digas un numero del 1 al 100
y te dira si es mas grande, si es mas pequeño
o lo has adivinado.
"""

import random
def adivina():
    a = random.randrange(0, 100)
    b =-1
    while a != b:
        b = int(input("Dime un numero del 0 al 100: "))
        if (a > b):
            print("El numero es mas grande que " + str(b))
        elif(a < b):
            print("El numero es mas pequeño que " + str(b))
        else:
            return("Has adivinado el numero, que crack!")

print(adivina())
