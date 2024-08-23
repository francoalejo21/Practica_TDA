from grafo import Grafo
""" Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, 
indique si es posible pintar cada vértice con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color. """

def colorear(grafo, n):
    #los colores son "numeros", ejemplo color amarillo = 0, color = rojo = 1,....
    colores = {} #diccionario de vertices coloreados
    vertices = grafo.obtener_vertices()

    for v in vertices: #por si hay mas de 1 componente conexa
        if not v in colores:
            colorear_rec(grafo, vertices[0], colores, n )
    return len(colores) == len(vertices) #Todos los vertices fueron coloreados

def colorear_rec(grafo, v, colores, n):
    
    for color in range(n): #itero sobre los colores
        colores[v] = color #pruebo pintando el vertice con un color

        if not es_compatible(grafo,colores,v):
            continue #solucion parcial inválida --> pinto con otro color
    
        correcto = True #pude pintar
      
        for w in grafo.adyacentes(v): 
            if not w in colores: # pinto un adyacente que no fue pintado
                if not colorear_rec(grafo, w, colores, n) : #solucion parcial inválida --> pinto con otro color
                    correcto = False
                    break
        if correcto:
            return True
    del colores[v]    #solucion parcial inválida -> vuelvo 
    return False

def es_compatible(grafo, colores, v):
    
    for w in grafo.adyacentes(v):
        if w in colores and colores[v] == colores[w]:
            return False
    return True

#ejemplo:
grafo = Grafo()
#1ra componente conexa
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_arista("A","B")
grafo.agregar_arista("C","B")

#2da componente conexa
grafo.agregar_vertice("D")
grafo.agregar_vertice("E")
grafo.agregar_vertice("F")
grafo.agregar_arista("D","E")
grafo.agregar_arista("E","F")
grafo.agregar_arista("D","F")

print(colorear(grafo,2))