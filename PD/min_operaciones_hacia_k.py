""" Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones 
posibles son:
(i) aumentar el valor del operando en 1;
(ii) duplicar el valor del operando.
Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a realizar 
(y cuáles son dichas operaciones). Desarrollar la ecuación de recurrencia. 
Indicar y justificar la complejidad del algoritmo implementado. Aclaración: asegurarse de que el algoritmo presentado sea de 
programación dinámica, con su correspondiente ecuación de recurrencia.

Devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2' """

# Ecuacion de recurrencia: Opt(k) = min (Opt(k/2) + 1 si K es par si no infinito, Opt(k-1) + 1)
def minima_cantidad_operaciones(k):
    
    if k == 0: return 0,[]
    if k == 1: return 1,["mas1"]
    if k == 2: return 2,["mas1", "mas1"] # Da lo mismo si es "mas1","por2"
    
    M = [0 for i in range(k+1)]
    M[0] = 0
    M[1] = 1
    M[2] = 2

    for i in range(3, k+1):
        opcion1 = 99999999 # 99999999 vendria a representar el infinito
        if i%2 == 0:
            l = i//2
            opcion1 = M[l] + 1
        opcion2 = M[i-1] + 1
        M[i] = min(opcion1, opcion2)
    
    operaciones = reconstruir_operaciones(M)
    return M[k], operaciones

def reconstruir_operaciones(M):
    operaciones = []
    k = len(M)-1
    while k > 0:
        k = int(k)
        opcion1 = 99999999 # 99999999 vendria a representar el infinito
        if k%2 == 0:
            r = k//2
            opcion1 = M[r] + 1
        opcion2 = M[k-1] + 1

        if opcion1 < opcion2:
            operaciones.append("por2")
            k/=2
        else:
            operaciones.append("mas1")
            k-=1
    operaciones.reverse()
    return operaciones

if __name__ == "__main__":
    # Ejemplo 
    k = 10
    print(minima_cantidad_operaciones(k))