from grafo import Grafo

#Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, 
# devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices 
# sea adyacente entre si.

def no_adyacentes(grafo, n):
    'Devolver una lista con los n vértices, o None de no ser posible'
    vertices = grafo.obtener_vertices()
    solucion_parcial = set()
    solucion, es_solucion = no_adyacentes_rec(grafo, vertices, 0, solucion_parcial, n)
    if es_solucion and n > 0 :
        return list(solucion)
    return None

def no_adyacentes_rec(grafo,vertices, vertice, solucion_parcial, n ):
    #if len(vertices) == vertice: #Ya probe todos los vertices de mi grafo y mi solucion es menor
    #    if len(solucion_parcial) < n :

    if len(solucion_parcial) == n : # si encontré mi subconjunto de tamaño n checkeo si es válido
        if es_valida_solucion(grafo, solucion_parcial): # checkeo si al agregar el vercite es válida la solución
            return solucion_parcial, True
        return None, False
    if not es_valida_solucion(grafo, solucion_parcial) or ya_no_llego(grafo, solucion_parcial,vertice,n): # si al agregar el vertice no puede ser valida bajo ningun punto mi solucion_parcial
        return solucion_parcial, False
    
    solucion_parcial.add(vertices[vertice]) #pruebo agregando el vertice 
    solucion, es_solucion = no_adyacentes_rec(grafo, vertices, vertice+1, solucion_parcial, n)
    if es_solucion: #es validá la solución entonces la devuelvo
        return solucion, es_solucion
    solucion_parcial.remove(vertices[vertice]) #pruebo sacando el vertice
    return no_adyacentes_rec(grafo, vertices, vertice+1, solucion_parcial, n)

def es_valida_solucion(grafo,solucion_parcial):
    for v in solucion_parcial:
        for w in grafo.adyacentes(v):
            if grafo.estan_unidos(v,w) and w in solucion_parcial:
                return False
    return True

def ya_no_llego(grafo,solucion_parcial,vertice,n):
    if len(solucion_parcial) +((len(grafo.obtener_vertices())) - vertice) < n :
        return True
    return False


#ejemplo:
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

grafo.agregar_arista("A","J")
grafo.agregar_arista("J","H")
grafo.agregar_arista("A","B")
grafo.agregar_arista("C","B")
grafo.agregar_arista("C","I")

grafo.agregar_arista("F","C")
grafo.agregar_arista("F","I")
grafo.agregar_arista("D","I")
grafo.agregar_arista("E","F")
grafo.agregar_arista("E","G")

""" grafo = Grafo()
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")

grafo.agregar_arista("A","B")
grafo.agregar_arista("B","C")
grafo.agregar_arista("B","E")
grafo.agregar_arista("C","E")
 """
print(no_adyacentes(grafo,6))