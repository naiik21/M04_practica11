def declaracio(): # declaramos la funcion
    edat = int(input("Escriu la teva edad:  "))  # pedimos la edat
    ingressos = int(input("Escriu els teus ingressos mensuals:  "))  # pedimos los ingresos
    if(edat >= 18 and ingressos > 1200): # si pasa las dos opciones returnara esto
        return "És necessari que facis la declaració d’hisenda"
    else: # si no returnara esto
        return "Encara no pots fer la declaració"

print(declaracio()) # imprimiamos por pantalla el resultado de la funcion
