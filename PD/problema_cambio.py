""" Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata. 
Se desea devolver el cambio pedido, usando la mínima cantidad de monedas/billetes. Implementar un algoritmo que, por programación dinámica, 
reciba un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y devuelva qué monedas/billetes deben ser utilizados 
para minimizar la cantidad total utilizda. Indicar y justificar la complejidad del algoritmo implementado.
Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por programación dinámica". Por las características de la herramienta, 
no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción """
#ejemplo monedas que recibo [1, 2, 3, 5, 15, 20, 50, 100] y se quiere dar cambio de 30 
#un algoritmo greedy que se basa en dar la mayor moneda posible en cada paso daría [20,5,5]
#pero la respuesta correcta sería dar [15, 15] que es la mínima cantidad de monedas posibles

#Complejidad temporal : 
# Ordenamiento : O(n*log(n)) donde n es la cantidad de monedas del sistema monetario
# Inicializacion de la matriz : O(n*m) donde n es la cantidad de monedas del sistema monetario y m es el cambio a dar
# Recorrido de la matriz : O(n*m) donde n es la cantidad de monedas del sistema monetario y m es el cambio a dar y se hacen operaciones de comparacion constantes
# Complejidad en totatl: O(n*m) donde n es la cantidad de monedas del sistema monetario y m es el cambio a dar

def cambio(monedas, monto):
    # Ecuacion de recurrencia: C[n, m ] = min (m // V(n) + C[n-1, m - (m // V(n))* V(n) ], C[n-1, m] )
    
    # donde n : cantidad de monedas del sistema monetario
    # donde m : cambio a dar
    
    # Casos_base:  C[0,m] = 0 , C[1,m] = m
    # //: division entera
    # restriccion que V(n) < m caso contrario la expresion:  [ m // V(n) + C[n-1, m - (m // V(n))* V(n) ] no vale 

    if not monedas: #No hay sistema monetario devuelvo nada
        return []
    monedas = sorted(monedas) #ordeno para que luego al poner mis casos bases sea cohererente
    matriz = inicializar_matriz(len(monedas)+1, monto+1) 
    matriz = poner_casos_base(matriz)
    for i in range(1, monto+1): 
        for j in range(1, len(monedas)+1):
            
            valor_moneda_j = monedas[j-1]
            
            if valor_moneda_j <= i:
                cant_monedas_j = i // valor_moneda_j
                matriz[i][j] = min(cant_monedas_j + matriz[i-cant_monedas_j*valor_moneda_j][j-1] , matriz[i][j-1])
            else:
                matriz[i][j] = matriz[i][j-1]
    
    return reconstruir_solucion(monto,len(monedas), monedas, matriz)



def inicializar_matriz(N,W):
    matriz = []
    for i in range(W):
        fila = []
        for j in range(N):
            fila.append(0)
        matriz.append(fila)
    return matriz

def poner_casos_base(matriz):
    monto = 1
    
    for i in range(1,len(matriz)):
        matriz[i][0] = monto
        monto+=1
    return matriz
def reconstruir_solucion(W, N, monedas, matriz):
    solucion = []
    while W >0 and N>0:
        
        valor_moneda = monedas[N-1]
        cant_monedas = W // valor_moneda
        
        # Verificar si esta moneda fue incluido en la solución
        if valor_moneda <= W and matriz[W][N] == cant_monedas + matriz[W - cant_monedas*valor_moneda][N - 1]:
            # Si fue incluido, agregamos el/las monedas  a la solución
            for _ in range(cant_monedas):
                solucion.append(valor_moneda)
            
            W -= cant_monedas*valor_moneda  # Reducimos la capacidad de la mochila
        N -= 1  # Seguimos con el siguiente elemento

    solucion.reverse()
    return solucion


def main():
    sistema_monetario = [1,  5]
    cambio_a_dar = 11
    print(cambio(sistema_monetario,cambio_a_dar))

if __name__ == "__main__":
    main()
