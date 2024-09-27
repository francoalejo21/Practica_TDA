""" Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. 
Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha. 
Pasar por un casillero determinado (i, j) nos da una ganancia de V_{i,j}. Implementar un algoritmo que, por programación dinámica, obtenga 
la máxima ganancia a través del laberinto. Hacer una reconstrucción del camino que se debe transitar. 
Indicar y justificar la complejidad del algoritmo implementado. Si hay algunos lugares por los que no podemos pasar (obstáculos), 
¿cómo se debe modificar para resolver el mismo problema?
Aclaración: solamente por simplicidad de las pruebas automáticas, devolver en este caso la ganancia máxima obtenible. Tener en cuenta que en un examen 
se pediría la reconstrucción de cómo se obtiene la ganancia.
Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción """

def laberinto(matriz):
    if not matriz or not matriz[0]: #si no tengo matriz la ganancia maxima es 0
        return 0
    
    N = len(matriz) #cant de filas
    M = len(matriz[0]) #cant de columnas
    
    matriz_memoizada = construir_matriz(N,M)
    matriz_memoizada = llenar_casos_bases(matriz, matriz_memoizada)
    
    for i in range(1,N):
        for j in range(1,M):
            matriz_memoizada[i][j] = max(matriz_memoizada[i-1][j] + matriz[i][j] , matriz_memoizada[i][j-1] + matriz[i][j] )
    N = N-1
    M = M-1
    # print(matriz_memoizada)  si quiero ver mi matriz memoizada
    return reconstruir_solucion(N,M,matriz_memoizada,matriz), matriz_memoizada[len(matriz_memoizada)-1][ len(matriz_memoizada[0])-1]

#Ecuacion de recurrencia: G[i][j] = max(G[i-1][j] + matriz[i][j],  G[i][j-1] + matriz[i][j] )

def reconstruir_solucion(N,M, matriz_memoizada, matriz):
    #volvemos a aplicar la ecuacion de recurrencia
    solucion = []
    while N >= 0 and M >= 0:
        if N == 0 and M == 0 :#Estoy en la posicion de inicio, la tengo que agregar si o si
            solucion.append((N,M))
            break
        vine_por_columna = matriz_memoizada[N-1][M] + matriz[N][M] if N>=0 else 0
        vine_por_fila = matriz_memoizada[N][M-1] + matriz[N][M] if M>=0 else 0
        if vine_por_columna > vine_por_fila:
            solucion.append((N,M))
            N -=1
        if vine_por_fila >= vine_por_columna:
            solucion.append((N,M))
            M-=1  
    solucion.reverse()
    return solucion

def construir_matriz(N,M):
    matriz  = []
    for i in range(N):
        fila = []
        for j in range(M):
            fila.append(0)
        matriz.append(fila)
    return matriz

def llenar_casos_bases(matriz, matriz_memorizada):
    #iterar la primera fila y llenarla de los numeros
    #iterar la primera columna y llenarla de los numeros
    for i in range(len(matriz[0])): ##lleno primera fila
        if i > 0:
            matriz_memorizada[0][i] =  matriz_memorizada[0][i-1]+ matriz[0][i]
        else:
            matriz_memorizada[0][i] = matriz[0][0]

    for i in range(len(matriz)): ##lleno primera columna
        if i > 0:
            matriz_memorizada[i][0] =  matriz_memorizada[i-1][0]+ matriz[i][0]
        else:
            matriz_memorizada[i][0] = matriz[0][0]
    return matriz_memorizada

#Caso de prueba :
#matriz 5X6:                    #solucion        

#[1, 1, 1, 1, 1, 1]     =>     #[1, 2,  3,  4,  5,  6] 
#[1, 3, 0, 2, 5, 8]            #[2, 5,  5,  7,  12, 20]
#[1, 7, 4, 1, 0, 5]            #[3, 12, 16, 17, 17, 25]
#[1, 9, 2, 0, 1, 9]            #[4, 21, 23, 23, 24, 34]
#[1, 0, 3, 4, 0, 0]            #[5, 21, 26, 30, 30, 34]

def main():
    matriz = [
        [1, 1, 1, 1, 1, 1],
        [1, 3, 0, 2, 5, 8],
        [1, 7, 4, 1, 0, 5],
        [1, 9, 2, 0, 1, 9],
        [1, 0, 3, 4, 0, 0], 
        ]
    camino_solucion, ganancia_maxima = laberinto(matriz)
    print(ganancia_maxima)
    print(camino_solucion)

main()