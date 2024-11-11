""" Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos

Dos grafos son isomorfos si tienen el mismo número de vértices y los vértices de cada grafo se pueden numerar de 1 
hasta n de modo que dos vértices del segundo grafo están unidos por una arista si y sólo si los dos vértices del primer grafo que
tienen los mismos números están unidos por una arista."""
from grafo import Grafo

def hay_isomorfismo(g1, g2):
    # Paso 1: Comprobar que ambos grafos tengan el mismo número de vértices
    if len(g1.obtener_vertices()) != len(g2.obtener_vertices()):
        return False

    # Paso 2: Calcular los grados de los vértices
    grados_g1 = calcular_grados_vertices(g1)
    grados_g2 = calcular_grados_vertices(g2)

    # Paso 3: Ordenar los vértices por grados
    vertices_g1 = sorted(grados_g1.items(), key=lambda x: x[1])
    vertices_g2 = sorted(grados_g2.items(), key=lambda x: x[1])

    # Si los grados no coinciden, los grafos no pueden ser isomorfos
    if [grado for _, grado in vertices_g1] != [grado for _, grado in vertices_g2]:
        return False

    # Paso 4: Inicializar listas de vértices y empezar la búsqueda recursiva
    vertices_g1 = [v for v, _ in vertices_g1]
    vertices_g2 = [v for v, _ in vertices_g2]
    
    # Diccionario para asignaciones de vértices de g1 a g2
    asignaciones = {}
    
    # Llamada a la función recursiva para buscar el isomorfismo
    return _hay_isomorfismo_rec(g1, g2, vertices_g1, vertices_g2, asignaciones)

def _hay_isomorfismo_rec(g1, g2, vertices_g1, vertices_g2, asignaciones):
    # Si hemos asignado todos los vértices, encontramos un isomorfismo
    if len(asignaciones) == len(vertices_g1):
        return True
    
    # Tomamos el siguiente vértice de g1 que no está asignado
    vertice_g1 = vertices_g1[len(asignaciones)]

    for vertice_g2 in vertices_g2:
        # Intentamos asignar vertice_g1 a vertice_g2 si es compatible
        if vertice_g2 not in asignaciones.values() and es_compatible_asignacion(g1, g2, asignaciones, vertice_g1, vertice_g2):
            # Asignamos y continuamos recursivamente
            asignaciones[vertice_g1] = vertice_g2
            if _hay_isomorfismo_rec(g1, g2, vertices_g1, vertices_g2, asignaciones):
                return True
            # Retrocedemos si la asignación no lleva a una solución
            del asignaciones[vertice_g1]

    # Si ninguna asignación es válida, retornamos False
    return False

def es_compatible_asignacion(g1, g2, asignaciones, vertice_g1, vertice_g2):
    # Verifica si al asignar vertice_g1 a vertice_g2 se mantienen las conexiones
    for vecino in g1.adyacentes(vertice_g1):
        if vecino in asignaciones:
            if not g2.estan_unidos(vertice_g2, asignaciones[vecino]):
                return False
    return True

def calcular_grados_vertices(g):
    grados = {}
    for v in g.obtener_vertices():
        grados[v] = 0
    for v in g.obtener_vertices():
        for w in g.adyacentes(v):
            if v == w:
                continue
            grados[v] += 1
    return grados