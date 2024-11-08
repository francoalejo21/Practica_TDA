""" Implementar un algoritmo tipo Backtracking que reciba una cantidad de dados n y una suma s. 
La función debe devolver todas las tiradas posibles de n dados cuya suma es s. Por ejemplo, con n = 2 y s = 7, 
debe devolver [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]. ¿De qué complejidad es el algoritmo en tiempo? ¿Y en espacio? """
def sumatoria_dados(n, s):
    tiradas_posibles = []
    tirada_actual = []
    _sumatoria_dados_rec(n,s,tirada_actual,tiradas_posibles)
    return tiradas_posibles

def _sumatoria_dados_rec(n,s,tirada_actual,tiradas_posibles):
    suma = suma_dados(tirada_actual)
    if len(tirada_actual) == n:
        if sum(tirada_actual) == s:
            tiradas_posibles.append(tirada_actual[:])  # Añadir una copia de la tirada actual
        return
        
    if len(tirada_actual) < n  and suma >= s or suma + (n - len(tirada_actual)) * 6 < s:
        return 
    
    for i in range(1,7):
        tirada_actual.append(i)
        _sumatoria_dados_rec(n,s,tirada_actual,tiradas_posibles)
        tirada_actual.pop()
    return

def suma_dados(tirada_actual):
    suma = 0
    for dado in tirada_actual:
        suma += dado
    return suma

if __name__ == "__main__":
    print(sumatoria_dados(10,55))