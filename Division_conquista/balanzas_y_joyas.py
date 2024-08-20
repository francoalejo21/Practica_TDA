from balanzas import balanza

def encontrar_joya(joyas):
    return encontrar_joya_rec(joyas, 0, len(joyas) - 1)

def encontrar_joya_rec(joyas, inicio, fin):
    # Caso base: si solo quedan dos joyas, compararlas directamente
    if fin - inicio == 1:
        peso = balanza([joyas[inicio]], [joyas[fin]])
        if peso == 1:
            return inicio
        else:
            return fin

    # Calcular la mitad del rango actual
    mitad = (inicio + fin) // 2

    # Dividir las joyas en dos mitades, incluyendo la joya del medio en ambas si es impar
    joyas_izq = joyas[inicio:mitad + 1]  # Incluye hasta la mitad
    joyas_der = joyas[mitad:fin + 1]     # Incluye desde la mitad

    # Evaluar las dos mitades con la balanza
    peso = balanza(joyas_izq, joyas_der)

    # Determinar cuál mitad contiene la joya verdadera
    if peso == 1:
        # La joya verdadera está en la primera mitad
        return encontrar_joya_rec(joyas, inicio, mitad)
    elif peso == -1:
        # La joya verdadera está en la segunda mitad
        return encontrar_joya_rec(joyas, mitad, fin)
    else:
        # Si ambas mitades pesan lo mismo, cualquier mitad es válida (pero seguimos buscando)
        return encontrar_joya_rec(joyas, inicio, mitad)

joyas = [0,0,0,0,0,0,0,0,0,0,1]
print(encontrar_joya(joyas))
