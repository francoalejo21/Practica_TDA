from balanzas import balanza

def encontrar_joya(joyas):
    return encontrar_joya_rec(joyas, 0, len(joyas) - 1)

def encontrar_joya_rec(joyas, inicio, fin):
    # Calcular la mitad del rango actual
    mitad = (inicio + fin) // 2
    
    # Caso base: si solo quedan dos joyas, compararlas directamente
    if (inicio + fin)%2 != 0: # solo hay dos joyas
        peso = balanza([joyas[inicio]], [joyas[fin]])
        if peso == 1:
            return inicio
        else:
            return fin
    if (inicio + fin)%2 == 0: #hay tres joyas
        peso = balanza([joyas[inicio]], [joyas[fin]]) # excluyo la joya del medio
        if peso == 1:
            return inicio
        elif peso == -1:
            return fin
        else: #como ninguna es la joya, no queda otra que sea la del medio
            return mitad

    # Determinar si la cantidad de joyas es impar
    es_impar = (fin - inicio + 1) % 2 != 0

    if es_impar:
        # Si es impar, excluimos la joya del medio
        peso = balanza(joyas[inicio:mitad], joyas[mitad + 1:])
        if peso == 0:
            return mitad  # La joya del medio es la verdadera
        elif peso == 1:
            # La joya verdadera está en la primera mitad
            return encontrar_joya_rec(joyas, inicio, mitad)    
        # La joya verdadera está en la segunda mitad
        return encontrar_joya_rec(joyas, mitad + 1, fin)

    else:
        # Si es par, comparamos las dos mitades
        peso = balanza(joyas[inicio:mitad + 1], joyas[mitad+1:fin + 1 ])

    # Evaluar el resultado de la balanza
    if peso == 1:
        # La joya verdadera está en la primera mitad
        return encontrar_joya_rec(joyas, inicio, mitad)
  
    # La joya verdadera está en la segunda mitad
    elif peso == -1:    
        return encontrar_joya_rec(joyas, mitad + 1, fin)


joyas = [0,0,1,0]
print(encontrar_joya(joyas))
