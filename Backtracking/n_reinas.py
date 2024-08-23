""" Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique (si es posible) a n reinas de tal 
manera que ninguna pueda comerse con ninguna.
Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe. """
def nreinas(n):
    solucion = set()  # Conjunto para almacenar las posiciones de las reinas
    es_solucion = nreinas_rec(n, solucion, 0)  # Comienza desde la fila 0
    return list(solucion)

def nreinas_rec(n, solucion, i_fila):
    if len(solucion) == n:  # Si se han colocado todas las reinas, la solución es válida
        return True
    
    for j in range(n):
        if (i_fila, j) in solucion or not es_compatible(solucion, i_fila, j):
            continue
        
        solucion.add((i_fila, j))  # Prueba colocando la reina en (i_fila, j)
        
        if nreinas_rec(n, solucion, i_fila + 1):  # Intenta colocar la siguiente reina en la siguiente fila
            return True
        
        solucion.remove((i_fila, j))  # Si no es posible, retira la reina y prueba en la siguiente columna
    
    return False

def es_compatible(solucion, fila, columna):
    for f, c in solucion:
        # Verificar si están en la misma columna o en la misma diagonal
        if c == columna or abs(f - fila) == abs(c - columna):
            return False
    return True

# Ejemplo de uso:
print(nreinas(4))  # Esto debería devolver una solución para el problema de las 4 reinas, como [(0, 1), (1, 3), (2, 0), (3, 2)]
