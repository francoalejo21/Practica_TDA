""" Dado un arreglo de n enteros, encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista.
Indicar y justificar la complejidad del algoritmo. """

def maximo_subarreglo(arreglo):
    return _maximo_subarreglo(arreglo, 0, len(arreglo)-1)

def _maximo_subarreglo(arreglo, inicio, fin):
    if inicio == fin:
        return [arreglo[inicio]], arreglo[inicio]
    
    medio = (inicio + fin) // 2

    arr_izq, suma_izq = _maximo_subarreglo(arreglo, inicio, medio)
    arr_der, suma_der = _maximo_subarreglo(arreglo, medio+1, fin)

    # Obtener el maximo subarreglo del medio en O(n)

    # Obtener el maximo subarreglo contiguo a izquierda que incluya el indice medio
    suma_max_izq = arreglo[medio]
    max_indice_izq = medio
    suma_actual_izq = arreglo[medio]

    for i in range(medio-1, inicio -1, -1):
        suma_actual_izq += arreglo[i]
        if suma_actual_izq > suma_max_izq:
            suma_max_izq = suma_actual_izq
            max_indice_izq = i
    
    # Obtener el maximo subarreglo contiguo a derecha que incluya el indice medio+1
    suma_max_der = arreglo[medio+1]
    max_indice_der = medio+1
    suma_actual_der = arreglo[medio+1]

    for i in range(medio+2, fin+1):
        suma_actual_der += arreglo[i]
        if suma_actual_der >suma_max_der:
            suma_max_der = suma_actual_der
            max_indice_der = i
    
    # subarreglo de suma maxima que pasa por el medio
    arr_medio, suma_medio = arreglo[max_indice_izq:max_indice_der+1], suma_max_izq + suma_max_der
    

    if suma_medio >= suma_izq and suma_medio >= suma_der:
        return arr_medio, suma_medio
    if suma_izq >= suma_medio and suma_izq >= suma_der:
        return arr_izq,suma_izq
    if suma_der >= suma_medio and suma_der >= suma_izq:
        return arr_der,suma_der

if __name__ == "__main__":
    # Ejemplo de prueba
    arreglo = [2, 3, -1, 3, -2, 5, -3, 1]
    subarreglo, suma = maximo_subarreglo(arreglo)
    print("Suma máxima:", suma)
    print("Subarreglo máximo:", subarreglo)