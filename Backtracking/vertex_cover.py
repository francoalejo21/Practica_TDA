"""Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un
mínimo Vertex Cover del mismo."""

from grafo import Grafo

def vertex_cover(grafo):
    aristas = buscar_aristas_dominadas(grafo.obtener_vertices(), grafo)
    vertices = grafo.obtener_vertices()
    return _vertex_cover(grafo, [], [vertices], 0, vertices, set(), aristas )

def _vertex_cover(grafo, solucion, mejor_solucion, indice, vertices, a_dominadas, aristas):
    
    # Poda: El tamaño de la solucion actual es mayor al de la mejor_solucion, no tiene sentido seguir explorando
    if len(solucion) > len(mejor_solucion[0]):
        return mejor_solucion[0]
    
    if len(a_dominadas) == len(aristas): # Se cubrieron todas las aristas del grafo
        mejor_solucion.clear()
        mejor_solucion.append(solucion.copy())
        return mejor_solucion[0]
    
    if indice >= len(vertices): # Llegamos al final de la lista de vertices y no se cubrieron todas las aristas con la solucion actual
        return mejor_solucion[0]

    # Poda: Si los vertices de mi solucion actual + los vertices que faltan explorar no llegan a dominar todas las aristas, no tiene sentido seguir explorando 
    aux = a_dominadas.copy()
    a_q_dominan = buscar_aristas_dominadas(vertices[indice:], grafo) # devuelve una lista de aristas
    for a in a_q_dominan:
        v,w = a
        if not (v,w) in aux and not (w,v) in aux:
            aux.add((v,w))
    if len(aux) != len(aristas):
        return mejor_solucion[0]
    
    nuevas_aristas_dominadas = []
    for w in grafo.adyacentes(vertices[indice]):
        if not (vertices[indice], w) in a_dominadas and not (w, vertices[indice]) in a_dominadas:
            nuevas_aristas_dominadas.append((vertices[indice],w))
    
    if nuevas_aristas_dominadas:
        for a in nuevas_aristas_dominadas:
            a_dominadas.add(a)
        
        # Agrego el vertice y llamo recursivamente
        solucion.append(vertices[indice])
        resultado1 = _vertex_cover(grafo, solucion, mejor_solucion, indice+1, vertices, a_dominadas, aristas)
        
        # Quito el vertico y llamo recursivamente
        solucion.pop()
        for a in nuevas_aristas_dominadas:
            a_dominadas.remove(a)
        resultado2 = _vertex_cover(grafo, solucion, mejor_solucion, indice+1, vertices, a_dominadas, aristas)

        if len(resultado1) < len(resultado2):
            return resultado1
        return resultado2
    return _vertex_cover(grafo, solucion, mejor_solucion, indice+1, vertices, a_dominadas, aristas)

def buscar_aristas_dominadas(vertices, grafo):
    aristas_dominadas = set()
    for v in vertices:
        for w in grafo.adyacentes(v):
            if not (v,w) in aristas_dominadas and not (w,v) in aristas_dominadas:
                aristas_dominadas.add((v,w))
    return aristas_dominadas

if __name__ == "__main__":
    # Ejemplo
    
    grafo = Grafo()
    grafo.agregar_vertice('A')
    grafo.agregar_vertice('B')
    grafo.agregar_vertice('C')
    grafo.agregar_vertice('D')
    grafo.agregar_vertice('E')

    grafo.agregar_arista('A', 'E')
    grafo.agregar_arista('B', 'E')
    grafo.agregar_arista('C', 'E')
    grafo.agregar_arista('D', 'E')

    print(vertex_cover(grafo))