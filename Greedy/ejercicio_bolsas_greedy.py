def bolsas(capacidad, productos):
    #precondicion necesaria: el producto mas pesado no supera la capacidad de la bolsa --> si no no tiene sentido el problema, nunca podriamos guardar todos
    #ejemplo : productos = [4, 2, 1, 3, 5]
    #capacidad = 5
    #debemos devolver una lista de bolsas que tienen los productos
    # [[1, 2], [3], [4], [5]]
    pesos_productos = sorted(productos)
    bolsas = [] #lista de bolsas usadas

    bolsa_i = [] #1ra bolsa vacia
    capacidad_bolsa_i = capacidad

    for peso in pesos_productos:
        if bolsa_i == []: #bolsa vacia
            bolsa_i.append(peso)
            capacidad_bolsa_i -= peso #resto capacidad a la bolsa
            continue
        if capacidad_bolsa_i - peso >= 0 : # si hay capacidad en la bolsa, la agrego
            bolsa_i.append(peso)
            capacidad_bolsa_i -= peso  #resto capacidad a la bolsa
        else: #si no hay capacidad, abro otra bolsa
            bolsas.append(bolsa_i) #"cierro la bolsa"
            
            bolsa_i = [] #"abro otra bolsa nueva"
            capacidad_bolsa_i = capacidad 
            bolsa_i.append(peso)
            capacidad_bolsa_i -= peso

    if bolsa_i:  # Aseguramos que la última bolsa se agregue a la lista
        bolsas.append(bolsa_i)

    return bolsas

def bolsasGPT(capacidad, productos):
    # Ordenar los productos en orden descendente para optimizar el espacio en cada bolsa
    productos.sort(reverse=True)
    bolsas = []

    for peso in productos:
        # Intentar ubicar el producto en la primera bolsa que tenga espacio disponible
        colocado = False
        for bolsa in bolsas:
            if sum(bolsa) + peso <= capacidad:
                bolsa.append(peso)
                colocado = True
                break

        # Si no hay bolsas con espacio, crear una nueva
        if not colocado:
            bolsas.append([peso])

    return bolsas

# Explicación bolsasGPT:
# Orden Descendente:
# Ordena los productos en orden descendente para intentar ubicar los productos más grandes primero, lo que reduce la cantidad de bolsas utilizadas.
# Primera Bolsa que Satisface la Condición:
# Para cada producto, intentamos colocarlo en la primera bolsa con suficiente capacidad, evitando así crear nuevas bolsas innecesariamente.
# Complejidad Temporal: O(n log n)
# Recorrido de las bolsas: El bucle interno tiene un peor caso de 𝑂(𝑚)*O(m) donde 𝑚 es el número de bolsas, pero en la práctica esto tiende a ser mucho menor que 𝑛, y suele ser constante.
# Complejidad Total: Sigue siendo 𝑂(𝑛 log𝑛) debido al ordenamiento, pero la implementación es más eficiente en términos de la cantidad de operaciones realizadas dentro del bucle.


productos = [4, 2, 1, 3, 5]
print(bolsas(5,productos))
print(bolsasGPT(5,productos)) #mas eficiente