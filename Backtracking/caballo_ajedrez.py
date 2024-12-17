
""" Implementar un algoritmo de backtracking que, dado una pieza de caballo en un tablero de ajedrez de n x n, determine si existen los movimientos a realizar para que el caballo logre pasar por todos los casilleros del tablero una única vez.
Recordar que el caballo mueve en forma de L (dos casilleros en una dirección, y un casillero en forma perpendicular). 

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe."""

def knight_tour(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    visitados = []
    for i in range(n):
        for j in range(n):    
            matriz[i][j] = 1
            visitados.append((i,j))
            if resolver_caballo(matriz, i, j, n , visitados): 
                return True
            matriz[i][j] = 0
            visitados.remove((i,j))            
    return False
            
def resolver_caballo(tablero, y, x,n, visitados):

    if len(visitados) == n*n: # si visité todos los casilleros del tablero
        return True

    # pruebo colocando en un casillero válido y que no fue visitado anteriormente
    movimientos_posibles = [(2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2), (-2, -1), (-2, 1)]
    for movimiento in movimientos_posibles: 
        if puedo_colocar(tablero, y, x, movimiento):
            
            posicion_nueva_y = y+movimiento[0]
            posicion_nueva_x = x+movimiento[1]
            

            tablero[posicion_nueva_y][posicion_nueva_x] = 1
            visitados.append((posicion_nueva_y, posicion_nueva_x))
            
            if resolver_caballo(tablero, posicion_nueva_y, posicion_nueva_x, n, visitados):
                return True
            
            tablero[posicion_nueva_y][posicion_nueva_x] = 0
            visitados.remove((posicion_nueva_y, posicion_nueva_x))
    
    return False   

def puedo_colocar(tablero, y, x, movimiento):
    # si se va fuera del tablero
    posicion_nueva_y = y + movimiento[0]
    posicion_nueva_x = x + movimiento[1]
    if posicion_nueva_y >= len(tablero) or  posicion_nueva_y < 0:
        return False
    if posicion_nueva_x >= len(tablero[0]) or posicion_nueva_x < 0:
        return False
    
    
    if tablero[posicion_nueva_y][posicion_nueva_x] == 1: # si ya fue visitado ese casillero
        return False

    return True
def main():
    print(knight_tour(7))  

if __name__ == "__main__":
    main()