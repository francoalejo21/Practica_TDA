def max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    max_left = 0

    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float('-inf')
    sum = 0
    max_right = 0

    for i in range(mid + 1, high + 1):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return max_left, max_right, left_sum + right_sum

def _max_subarray(arr, low, high):
    if low == high:
        return low, high, arr[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = _max_subarray(arr, low, mid)
    right_low, right_high, right_sum = _max_subarray(arr, mid + 1, high)
    cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

arreglo = [200, 9, 100, -150, 150]
low, high, max_sum = max_subarray(arreglo, 0, len(arreglo) - 1)
print("El máximo subarray contiguo es:", arreglo[low:high + 1], "con suma:", max_sum)





def max_subarray(arr):
    _, max_sub = _max_subarray(arr, 0)
    return max_sub

def max_medio(arr):
    # Aquí calculamos el máximo subarray que cruza la mitad del array
    suma = 0
    max_suma = float('-inf')
    max_izq = 0
    max_der = 0
    izq = 0

    for i in range(len(arr) - 1, -1, -1):
        suma += arr[i]
        if suma > max_suma:
            max_suma = suma
            max_izq = i

    suma = 0
    max_suma = float('-inf')

    for i in range(len(arr)):
        suma += arr[i]
        if suma > max_suma:
            max_suma = suma
            max_der = i

    return max_suma, arr[max_izq:max_der + 1]  # Retorna la suma máxima y el subarray correspondiente

def comparador(arr_der, max_der, arr_medio, max_medio, arr_izq, max_izq):
    if max_der > max_medio:
        if max_der > max_izq:
            return max_der, arr_der
    
    elif max_medio > max_izq:
        if max_medio > max_der:
            return max_medio, arr_medio
    
    return max_izq, arr_izq


def _max_subarray(arr, maximo):
    if len(arr) == 1:
        return arr[0], arr  # Devuelve el número máximo del subarr y el subarr máximo

    mitad = len(arr) // 2

    max_izq, arr_izq = _max_subarray(arr[0:mitad], maximo)
    max_med, arr_med = max_medio(arr)  
    
    max_der, arr_der = _max_subarray(arr[mitad:], maximo)

    max_global, arr_global = comparador(arr_der, max_der, arr_med, max_med, arr_izq, max_izq)

    return max_global, arr_global


def main():
    "max subarray mixto 6 elementos"
    arreglo = [200,9,100,-150,150]
    print(max_subarray(arreglo))

main()