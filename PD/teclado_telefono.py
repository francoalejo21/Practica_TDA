""" Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad de posibles números de longitud N
empezando por botón del número inicial k. 
Restricción: 
solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual. 

Implementar el algoritmo por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. 
Ejemplos:

Para n=1 empezando por cualquier dígito, solamente hay un número válido (el correspondiente dígito)
Para N=2, depende de cuál dígito se comienza.
Empezando por 0, son válidos 00, 08 (cantidad: 2)
Empezando por 1, son válidos 11, 12, 14 (cantidad: 3)
Empezando por 2, son válidos 22, 21, 23, 25 (cantidad: 4)
Empezando por 3, son válidos 33, 32, 36 (cantidad: 3)
Empezando por 4, son válidos 44, 41, 45, 47 (cantidad: 4)
Empezando por 5, son válidos 55, 52, 54, 56, 58 (cantidad: 5)
Empezando por 6, son válidos 66, 63, 65, 69 (cantidad: 4)
Empezando por 7, son válidos 77, 74, 78 (cantidad: 3)
Empezando por 8, son válidos 88, 80, 85, 87, 89 (cantidad: 5)
Empezando por 9, son válidos 99, 96, 98 (cantidad: 3)
Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe. """

#Ecuacion de recurrencia : C(n,k) = C[n-1,k] +  [ sumatoria( C(n-1 , j))   con j perteneciente adyacentes de k ]
# siendo: caso base C(0,k) = 1   (forma trivial no hacer nada)            y C(1,k) = 1
#  k =  el numero por el que se empieza
#  n = longitud del numero
def numeros_posibles(k, n):
    N = n + 1  # Considera que n es la longitud del número
    matriz_memoizada = construir_matriz(N, 10)
    adyacentes = adyacentes_numeros()
    
    # Caso base: para n = 1, cada número tiene una única opción
    for i in range(10):
        matriz_memoizada[1][i] = 1
    
    for i in range(2, N):  # Empieza desde 2 porque la fila 1 ya está inicializada
        for j in range(10):
            matriz_memoizada[i][j] = matriz_memoizada[i-1][j] + sumatoria(adyacentes[j], matriz_memoizada, i-1)
    
    # Retornamos la suma de todas las posibilidades para la longitud 'n'
    return matriz_memoizada[N-1][k]


def adyacentes_numeros():
    dic = {}
    dic[0] = [8]
    dic[1] = [2, 4]
    dic[2] = [1, 3, 5]
    dic[3] = [2, 6]
    dic[4] = [1, 5, 7]
    dic[5] = [2, 4, 6, 8]
    dic[6] = [3, 5, 9]
    dic[7] = [4, 8]
    dic[8] = [0, 5, 7, 9]
    dic[9] = [6, 8]
    return dic


def sumatoria(adyacentes, matriz_memo, indice_solucion_menor):
    suma = 0
    for adyacente in adyacentes:
        suma += matriz_memo[indice_solucion_menor][adyacente]
    return suma


def construir_matriz(N, K):
    return [[0] * K for _ in range(N)]



#ejemplo
def main():
    print(numeros_posibles(1,3))

main()