"""
En esta funcion se pediran dos numeros
y te dira cual de ellos es mas grande.
"""

def masGrande():
    A = int(input("Dime un numero: "))
    B = int(input("Dime otro numero: "))
    if(A > B):
        return ("El numero " + str(A) + " es mas grande que " + str(B))
    elif(B > A):
        return ("El numero " + str(B) + " es mas grande que " + str(A))
    else:
        return ("Los dos numero son iguales")

print(masGrande())