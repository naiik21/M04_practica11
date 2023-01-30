def parellOSenar(): # declaramos la funcion
    a = int(input("Dime un numero:  "))
    if(a%2==0): # si a es parell
        return "El numero " + str(a) + " es parell"
    if(a%2!=0): # si a es senar
        return "El numero " + str(a) + " es senar"

print(parellOSenar()) # imprimiamos por pantalla el resultado de la funcion
