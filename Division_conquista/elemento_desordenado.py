def elemento_desordenado(arr):
    if len(arr) < 2:
        return None
    return elemento_desordenado_rec(arr, 0, len(arr) - 1)

def elemento_desordenado_rec(arr, inicio, final):
    if inicio >= final:
        return None
    
    medio = (inicio + final) // 2

    # Verificar si el elemento del medio está desordenado
    if medio > 0 and arr[medio] < arr[medio - 1]:  # Si el medio es menor que el anterior
        return arr[medio - 1]
    if medio < len(arr) - 1 and arr[medio] > arr[medio + 1]:  # Si el medio es mayor que el siguiente
        return arr[medio]

    # Verificar si el primer elemento está desordenado
    if inicio == 0 and arr[inicio] > arr[inicio + 1]:
        return arr[inicio]

    # Buscar en la parte izquierda
    izq = elemento_desordenado_rec(arr, inicio, medio)
    if izq is not None:
        return izq

    # Buscar en la parte derecha
    return elemento_desordenado_rec(arr, medio + 1, final)

if __name__ == "__main__":
    # Ejemplo de uso
    arreglo = [1, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(elemento_desordenado(arreglo))  # Output: 11