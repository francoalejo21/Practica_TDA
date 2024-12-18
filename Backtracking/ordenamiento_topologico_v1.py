""" Implementar un algoritmo que, por backtracking, obtenga la cantidad total de posibles ordenamientos topológicos 
de un grafo dirigido y acíclico. """

# A diferencia de la otra version que era de buscar todos los posibles ordenamientos topologicos que en complejidad espacial
# termina siendo exponencial por el arreglo de soluciones que se usaba

# esta implementacion ocupa espacio lineal principalmente por el diccionario de grados de entrada que ocupa O(n) siendo n
# la cantidad de vertices del grafo

from grafo import Grafo
def contar_ordenamientos(grafo):
    if len(grafo.obtener_vertices()) == 0:
        return 0
    grados_entrada = calcular_grados_vertices(grafo)
   
    k = len(grafo.obtener_vertices())
    n = [0]
    _contar_ordenamientos_rec(k, grafo, [], n, grados_entrada)
    return n[0]

def _contar_ordenamientos_rec(k, grafo, solucion, n, grados_entrada):
    
    if len(solucion) == k: # si encontré un ordenamiento válido que recorre todos los vertices
        n[0] +=1 #actualizo la cantidad de ordenamientos encontrados
        return
    
    vertices_posibles_a_agregar = []
    for v ,grado in grados_entrada.items():
        if grado == 0: # si el grado de entrada del vertice es cero entonces es posible empezar por ese
            vertices_posibles_a_agregar.append(v)
    
    for v in vertices_posibles_a_agregar:
        solucion.append(v) 
        # actualizo los grados de entrada de los vertices adyacentes
        actualizar_grados_entrada(grafo, v, grados_entrada, -1)
        grados_entrada[v] = -1 # marco como invalido para futuras exploraciones de vertices posibles        
        _contar_ordenamientos_rec(k, grafo, solucion, n,  grados_entrada)

        solucion.pop()
        actualizar_grados_entrada(grafo, v, grados_entrada, 1)
        grados_entrada[v] = 0 # restauro el vertice y lo pongo como valido
    
    return # si llegué acá es por que no hay vertices con grado de entrada 0

def actualizar_grados_entrada(grafo, v, grados_entrada, valor):
    for w in grafo.adyacentes(v):
        grados_entrada[w] += valor

def calcular_grados_vertices(grafo):
    grados_entrada = {}
    for v in grafo.obtener_vertices():
        grados_entrada[v] = 0

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grados_entrada[w] += 1
    return grados_entrada

def main():
    grafo  = Grafo(True)
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_vertice("E")
    grafo.agregar_vertice("F")
    grafo.agregar_vertice("G")
    grafo.agregar_vertice("H")

    grafo.agregar_arista("A","B")
    grafo.agregar_arista("C","B")
    grafo.agregar_arista("B","D")
    grafo.agregar_arista("B","E")
    grafo.agregar_arista("D","G")
    grafo.agregar_arista("D","F")
    grafo.agregar_arista("E","G")
    grafo.agregar_arista("E","H")
    print(contar_ordenamientos(grafo))

if __name__ == "__main__":
    main()