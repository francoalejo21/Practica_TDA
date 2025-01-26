"""
Implementar un algoritmo que reciba un grafo y un numero k y devuelva un dominating set de dicho grafo de a lo sumo 
k vertices si existe
"""
from grafo import Grafo

def dominating_set(grafo, k):
    vertices = grados(grafo) # Preprocesamiento para optimizar un poco y empezar por los mas prometedores que son los de mayor grado
    vertices = list(sorted(vertices,key= lambda x:x[1],reverse=True))
    vertices = [v for v,w in vertices]
    return _dominating_set(grafo, vertices, 0, [], k)

def _dominating_set(grafo, vertices, indice, solucion_actual, k):
    
    # Poda: mi cantidad de vertices de la solucion es mayor a k
    if len(solucion_actual) > k:
        return []
    
    #Poda : con los vertices que tengo y los restantes por explorar no es posible formar un dominating set
    if not es_dominating_set(solucion_actual+vertices[indice:], grafo):
        return []
    
    if es_dominating_set(solucion_actual, grafo):
        return solucion_actual

    if indice >= len(grafo.obtener_vertices()):
        return []

    solucion_actual.append(vertices[indice])
    solucion = _dominating_set(grafo, vertices, indice+1, solucion_actual, k)
    if solucion:
        return solucion
    solucion_actual.pop()
    return _dominating_set(grafo, vertices, indice+1, solucion_actual, k)

def es_dominating_set(solucion_actual, grafo):
    vertices = set()
    for v in solucion_actual:
        vertices.add(v)
        for w in grafo.adyacentes(v):
            vertices.add(w)
    return len(vertices) == len(grafo.obtener_vertices())

def grados(grafo):
    grados = {}
    for v in grafo.obtener_vertices():
        grados[v] = 0    
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grados[v] +=1
    vertices = []
    for v,grado in grados.items():
        vertices.append((v,grado))
    return vertices

if __name__ == "__main__":
    # Prueba
    grafo = Grafo()
    k = 2
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_vertice("E")
    grafo.agregar_vertice("F")
    grafo.agregar_vertice("G")
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("A", "E")
    grafo.agregar_arista("F", "E")
    grafo.agregar_arista("C", "E")
    grafo.agregar_arista("B", "G")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("G", "D")
    print(dominating_set(grafo, k))