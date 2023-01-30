"""
En esta funcion te pedira que digas
uno de los 5 nombres de la lista
y en cada uno te dira una frase diferente.
"""
def nombre():
    nombres = ["Messi", "Pedro", "Lebron", "Lewis", "Tommy"]
    print(nombres)
    pregunta = input("Dime uno de los nombres que sale en la lista: ")
    if(pregunta == "Messi"):
        print("Messi: El placer y la acción hacen que las horas parezcan cortas. ")
    elif(pregunta == "Pedro"):
        print("Pedro: Solo hay una felicidad en la vida – amar y ser amado.")
    elif (pregunta == "Lebron"):
        print("Lebron: Cuando el hombre no se encuentra a sí mismo, no encuentra nada.")
    elif (pregunta == "Lewis"):
        print("Lewis: No busques los errores, busca un remedio.")
    elif (pregunta == "Tommy"):
        print("Tommy: La muerte destroza al hombre: la idea de la muerte le salva.")
    else:
        print("El nombre que has seleccionado no esta entre la lista")

nombre()