""" Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la 
capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. 
Implementar un algoritmo que, por programación dinámica, reciba los valores y pesos de los elementos, y devuelva qué 
elementos deben ser guardados para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado.
Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con 
dicha restricción """

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    if not elementos: #No hay elementos devuelvo nada
        return []

    matriz = inicializar_matriz(len(elementos)+1, W+1) 
    for i in range(1, W+1): 
        for j in range(1, len(elementos)+1):
            
            valor,peso = elementos[j-1]
            if peso <= i:
                matriz[i][j] = max(valor + matriz[i-peso][j-1] , matriz[i][j-1])
            else:
                matriz[i][j] = matriz[i][j-1]
    
    return reconstruir_solucion(W,len(elementos), elementos, matriz)



def inicializar_matriz(N,W):
    matriz = []
    for i in range(W):
        fila = []
        for j in range(N):
            fila.append(0)
        matriz.append(fila)
    return matriz

def reconstruir_solucion(W, N, elementos, matriz):
    solucion = []
    while W >0 and N>0:
        
        elemento = elementos[N-1]
        valor, peso = elemento
        
        # Verificar si este elemento fue incluido en la solución
        if peso <= W and matriz[W][N] == valor + matriz[W - peso][N - 1]:
            # Si fue incluido, agregamos el elemento a la solución
            solucion.append(elemento)
            W -= peso  # Reducimos la capacidad de la mochila
        N -= 1  # Seguimos con el siguiente elemento


    solucion.reverse()
    return solucion

def main():
    elementos = [(8,2), (3,5), (8,7), (5,3), (6,2), (4,1)]
    #elementos = [(5,10)]
    W = 10
    print(mochila(elementos, W))

if __name__ == "__main__":
    main()