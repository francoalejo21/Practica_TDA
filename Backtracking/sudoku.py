def resolver_sudoku(matriz):
    casilleros_disponibles = posibles_casilleros(matriz)
    subgrupos = construir_subgrupos_3_x_3(matriz)
    numeros_disp_por_casillero = posibles_numeros_por_casillero(casilleros_disponibles, matriz, subgrupos)
    resolver_sudoku_bt(matriz, casilleros_disponibles, subgrupos, numeros_disp_por_casillero)
    return matriz

def resolver_sudoku_bt(matriz, casilleros_disponibles, subgrupos, numeros_disp_por_casillero):
    
    if not casilleros_disponibles:  # Caso base: si no hay más casilleros, el Sudoku está resuelto
        return True
    
    casillero, posibilidades = calcular_casillero_con_menos_posibilidades(numeros_disp_por_casillero)
    i, j = casillero
    
    if len(posibilidades) == 0:  # Si no hay posibilidades para este casillero, retrocede
        return False

    for posibilidad in posibilidades:
        #colocamos un posible numero
        matriz[i][j] = posibilidad
        #saco el casillero de las posibilidades
        casilleros_disponibles.remove(casillero)
        #actualizo posibles numeros por casillero
        numeros_disp_por_casillero = posibles_numeros_por_casillero(casilleros_disponibles, matriz, subgrupos)
        if resolver_sudoku_bt(matriz, casilleros_disponibles, subgrupos, numeros_disp_por_casillero):
            return True
        #no hubo forma de completar el sudoku con esta posibilidad
        #hago el backtrack
        casilleros_disponibles.add(casillero)
        # Si la opción no es válida, hacer backtracking
        matriz[i][j] = 0  # Revertir el cambio en la matriz
        numeros_disp_por_casillero = posibles_numeros_por_casillero(casilleros_disponibles, matriz, subgrupos)
        casilleros_disponibles.add(casillero)  # Reagregar el casillero a los disponibles
    
    return False
   




def calcular_casillero_con_menos_posibilidades(posibles_numeros_por_casillero):
    minimo = 10 #arbitrario
    casilla = []
    posibilidades_casillero = []
    for casillero , posibilidades_casilla in posibles_numeros_por_casillero.items():
        if len(posibilidades_casilla) < minimo:
            minimo = len(posibilidades_casilla)
            casilla = casillero
            posibilidades_casillero = posibilidades_casilla
    return casilla, posibilidades_casillero


def posibles_casilleros(matriz):
    posibles_casilleros = set()
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == 0:
                posibles_casilleros.add((i, j))
    return posibles_casilleros

def posibles_numeros_por_casillero(posibles_casilleros, matriz, subgrupos):
    posibilidades_por_casillero = {}
    for casillero in posibles_casilleros:
        i, j = casillero
        indice_subgrupo = encontrar_indice_subgrupo_pertenece(subgrupos, (i,j))
        subgrupo = subgrupos[indice_subgrupo]
        posibles_numeros = posibilidades(matriz,(i, j), subgrupo)
        posibilidades_por_casillero[(i,j)] = posibles_numeros
    return posibilidades_por_casillero

def posibilidades(matriz,posicion , subgrupo ):
    posibilidades = []
    numeros_ya_puestos = set()
    i , j = posicion
    for k in range(9): #numeros ya puestos por fila
        numero = matriz[i][k]
        if numero != 0 :
            numeros_ya_puestos.add(numero)
    for k in range(9): #numeros ya puestos por columna
        numero = matriz[k][j]
        if numero != 0 :
            numeros_ya_puestos.add(numero)

    for (i,j) in subgrupo: #numeros ya puestos en grupo 3x3
        numero = matriz[i][j]
        if numero != 0 :
            numeros_ya_puestos.add(numero)

    for i in range(1,10):
        if not i in numeros_ya_puestos:
            posibilidades.append(i)
    return posibilidades

def construir_subgrupos_3_x_3(matriz):
    subgrupos = [[] for _ in range(9)]  # Crear 9 subgrupos vacíos
    for i in range(9):
        for j in range(9):
            # Calcular el índice del subgrupo en el que caerá la celda (i, j)
            subgrupo_index = (i // 3) * 3 + (j // 3)
            subgrupos[subgrupo_index].append((i, j))  # Agregar la coordenada (i, j), no el valor
    return subgrupos

def encontrar_indice_subgrupo_pertenece(subgrupos, posicion):
    for index, subgrupo in enumerate(subgrupos):
        for (i, j) in subgrupo:
            if (i, j) == posicion:
                return index

##########################################################
# Interfaz grafica para visualizar la matriz
def imprimir_matriz(matriz):
    print("-" * 25)
    for i in range(9):
        fila = ""
        for j in range(9):
            if j % 3 == 0:
                fila += " | "
            fila += str(matriz[i][j]) + " "
        print(fila + "|")
        if (i + 1) % 3 == 0:
            print("-" * 25)

def visualizar_sudoku(matriz, funcion_backtracking):
    print("Sudoku sin resolver:")
    imprimir_matriz(matriz)

    #Resolver el Sudoku
    resolver_sudoku(matriz)
    print("Sudoku resuelto:")
    imprimir_matriz(matriz)
##########################################################
#Sudoku A           
#|1 | 3|  |  |  |  | 8|  | 9|
#|  | 2|  |  |  |  |  |  |  |
#|  |  |  |  | 4|  |  |  |  |
#|  |  |  |  |  |  |  |  |  |
#|9 |  |  | 2|  |  | 1|  |  |
#|  |  |  |  |  |  |  |  |  |
#|  |  |  | 7|  |  |  |  |  |
#|5 |  |  |  |  |  |  |  |  |
#|  | 4|  |  |  |  | 2|  |  |

#Ejemplo resolver el Sudoku A
def main():
    matriz = [[0 for _ in range(9)] for _ in range(9)]
    posiciones = [((0,0), 1), ((0,1), 3), ((0,6), 8), ((0,8), 9), ((1,1), 2), ((2,4), 4), ((4,0), 9), ((4,3), 2), 
    ((4,6), 1), ((6,3), 7), ((7,0), 5), ((8,1), 4), ((8,6), 2)]
    for (posicion, numero) in posiciones:
        i,j = posicion
        matriz[i][j] = numero
    visualizar_sudoku(matriz, resolver_sudoku)

main()