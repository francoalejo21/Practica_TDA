""" Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto
 de vértices que representen un máximo Independent Set del mismo. """
from grafo import Grafo
def independent_set(grafo):
    vertices = grafo.obtener_vertices()
    solucion = []
    mejor_solucion = []
    independent_set_rec(grafo, mejor_solucion, solucion, vertices, 0 )
    return len(mejor_solucion)

def independent_set_rec(grafo, mejor_solucion, solucion, vertices, v ):
    if len(vertices) == v: #Caso base: Ya recorri todos los vertices
        if es_independent_set(grafo, solucion):
            if len(solucion) > len(mejor_solucion):
                mejor_solucion.clear()
                mejor_solucion.extend(solucion)
        return mejor_solucion
    
    solucion.append(vertices[v]) #pruebo agregando un vertice
    if es_independent_set(grafo, solucion):
        if len(solucion) > len(mejor_solucion):
            mejor_solucion.clear()
            mejor_solucion.extend(solucion)     
        independent_set_rec(grafo, mejor_solucion, solucion, vertices, v+1)       
    solucion.pop() #pruebo quitando un vertice
    return independent_set_rec(grafo, mejor_solucion, solucion, vertices, v+1)

def es_independent_set(grafo, solucion):
    for v in solucion:
        for w in solucion:
            if v == w :
                continue
            if grafo.estan_unidos(v,w):
                return False
    return True

#Caso de prueba
grafo = Grafo()
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_vertice("D")
grafo.agregar_vertice("E")
grafo.agregar_vertice("F")
grafo.agregar_vertice("G")
grafo.agregar_vertice("H")
grafo.agregar_vertice("I")
grafo.agregar_vertice("J")
grafo.agregar_vertice("K")

grafo.agregar_arista("A","B")
grafo.agregar_arista("A","C")
grafo.agregar_arista("B","D")
grafo.agregar_arista("C","E")
grafo.agregar_arista("D","E")
grafo.agregar_arista("E","G")
grafo.agregar_arista("E","F")
grafo.agregar_arista("G","H")
grafo.agregar_arista("F","I")
grafo.agregar_arista("G","K")
grafo.agregar_arista("F","J")

print(independent_set(grafo))