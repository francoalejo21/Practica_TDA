""" Modificar el algoritmo anterior(suma_a_n.py) para que, dada una lista de enteros positivos L y un entero n, devuelva un subconjunto de L 
que sume exactamente n, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de n. """
def max_sumatoria_n(lista, n):
    subconjunto_maximo = []
    _sumatoriras_n_rec(lista,n,0,subconjunto_maximo,[])
    return subconjunto_maximo
    
def _sumatoriras_n_rec(lista,n,indice,subconjunto_maximo,subconjunto_actual):
    suma_sub_actual = sum(subconjunto_actual)
    suma_sub_max = sum(subconjunto_maximo)
    if indice == len(lista):
        if suma_sub_actual > suma_sub_max and suma_sub_actual <= n :
            subconjunto_maximo.clear()
            subconjunto_maximo.extend(subconjunto_actual)
        return
    if suma_sub_actual > suma_sub_max and suma_sub_actual <= n :
        subconjunto_maximo.clear()
        subconjunto_maximo.extend(subconjunto_actual)
    if suma_sub_actual > n:
        return
    
    #pruebo agregando el elemento al subconjunto_actual
    subconjunto_actual.append(lista[indice])
    _sumatoriras_n_rec(lista,n, indice+1, subconjunto_maximo,subconjunto_actual)

    #pruebo quitando el elemento del subconjunto_actual
    subconjunto_actual.pop()
    _sumatoriras_n_rec(lista,n, indice+1, subconjunto_maximo,subconjunto_actual)
    return

if __name__ == "__main__":   
    lista = [35,4,2]
    n = 38
    print(max_sumatoria_n(lista,n))