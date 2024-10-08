
""" Un camino hamiltoniano, es un camino de un grafo, que visita todos los vértices del grafo una sola vez. 
Implementar un algoritmo por backtracking que encuentre un camino hamiltoniano de un grafo dado. """

def camino_hamiltoniano(grafo):
    visitados = set()
    vertices = grafo.obtener_vertices()
    for v in vertices:
        camino, hay_camino = camino_hamiltoniano_rec(v, visitados, grafo, vertices, [])
        if hay_camino:
            break
    return camino

def camino_hamiltoniano_rec( v, visitados, grafo, vertices, camino):
    visitados.add(v) #agrego a los visitados
    camino.append(v) #agrego a mi posible camino hamiltoniano
    if len(camino) == len(vertices):
        return camino, True
    
    for w in grafo.adyacentes(v):
        if not w in visitados:
            camino, hay_camino= camino_hamiltoniano_rec(w, visitados, grafo, vertices, camino)
            if hay_camino:
                return camino, hay_camino
                
    #No hay mas adyacentes y no completamos el camino con todos los vertices
    visitados.remove(v) 
    camino.pop()
    return camino, False