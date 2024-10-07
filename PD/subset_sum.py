""" Tenemos un conjunto de números v_1, v_2, …, v_n, y queremos obtener un subconjunto de todos esos números tal que su 
suma sea igual o menor a un valor V, tratando de aproximarse lo más posible a V. 
Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores, y la suma objetivo V, y devuelva 
qué elementos deben ser utilizados para aproximar la suma lo más posible a V, sin pasarse. 
Indicar y justificar la complejidad del algoritmo implementado.
Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con
dicha restricción """
import problema_mochila
def subset_sum(elementos, v):
    #transformar el problema en un problema de la mochila, donde los elementos son los valores de los elementos 
    # y los pesos son los mismos valores
    # la ecuacion de recurrencia es: M[i,j] = max(M[i-1,j], M[i-1, j - elementos[i]] + elementos[i])
    # donde i es la cantidad de elementos y j es el valor objetivo
    # caso base: M[0,j] = 0, M[i,0] = 0
    # Complejidad temporal :
    # Inicializacion de la matriz : O(n*m) donde n es la cantidad de elementos y m es el valor objetivo
    # Recorrido de la matriz : O(n*m) donde n es la cantidad de elementos y m es el valor objetivo y se hacen operaciones de comparacion constantes
    # Complejidad en total: O(n*m) donde n es la cantidad de elementos y m es el valor objetivo
    elementos = transformar_elementos(elementos)
    solucion = problema_mochila.mochila(elementos, v)
    solucion = [elemento[0] for elemento in solucion] #saco los pesos de los elementos
    return solucion

def transformar_elementos(elementos):#transforma los elementos en tuplas (valor, peso), donde valor = peso
    elementos_nuevos = []
    for elemento in elementos:
        elementos_nuevos.append([elemento, elemento])
    return elementos_nuevos