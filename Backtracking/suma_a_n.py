""" Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L y un entero n devuelva todos los 
subconjuntos de L que suman exactamente n. """
def sumatorias_n(lista, n):
    subconjuntos = []
    _sumatoriras_n_rec(lista,n,0,[],subconjuntos)
    return subconjuntos

def _sumatoriras_n_rec(lista,n,indice,subconjunto_actual,subconjuntos):
    if indice == len(lista):
        if suma(subconjunto_actual) == n:
            subconjuntos.append(subconjunto_actual[:])
        return
    if suma(subconjunto_actual) == n:
        subconjuntos.append(subconjunto_actual[:])
        return
    if suma(subconjunto_actual) > n:
        return
    #pruebo agregando el elemento al subconjunto_actual
    subconjunto_actual.append(lista[indice])
    _sumatoriras_n_rec(lista,n, indice+1, subconjunto_actual, subconjuntos)

    #pruebo quitando el elemento del subconjunto_actual
    subconjunto_actual.pop()
    _sumatoriras_n_rec(lista,n, indice+1, subconjunto_actual, subconjuntos)

    return
 
def suma(subconjunto):
    suma = 0
    for elemento in subconjunto:
        suma+=elemento
    return suma

if __name__ == "__main__":   
    lista = [1,8,5,3,7,6,2]
    n = 8
    print(sumatorias_n(lista,n))

