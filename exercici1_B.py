def mesGran(): # declaramos la funcion
    a = int(input("Dime un numero:  "))
    b = int(input("Dime un numero:  "))
    if(a>b): # si a es mas grande que b
        return "El numero més gran es a:" + str(a) + " y el mes petit b:" + str(b)
    elif(a<b): # si b es mas grande que a
        return "El numero més gran es b:" + str(b) + " y el mes petit a:" + str(a)
    else: # si a y b son iguales
        return ""

print(mesGran())