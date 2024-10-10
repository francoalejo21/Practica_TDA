""" Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P que no puede 
sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La campaña i cuesta Ci. También se han realizado 
diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña, que denominaremos Gi. 
Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos. 
Indicar y justificar la complejidad del algoritmo propuesto. ¿Da lo mismo si los valores están expresados en pesos argentinos,
dólares u otra moneda? Por ejemplo, si una campaña cuesta 100 dólares, para pasar a pesos se debe hacer la conversión de 
divisa.
Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". 
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con 
dicha restricción """

# cada campaña publicitaria i de la forma (Gi, Ci)

# Podemos reducir este problema al problema de la mochila, donde el presupuesto P vendria a ser la capacidad total de mi mochila
# cada campaña representa un elemento de la mochila, donde cada campaña tiene una ganancia y costo 
# que transformado a mi problema de la mochila, cada cada ganancia se mapea a el valor de cada elemento de la mochila
# y cada costo de campaña se mapea a el peso de cada elemento de mi mochila

# Luego de hacer esta transformacion de mi problema y adaptando mi problema a la entrada de mi caja resolvedora del problema
# de la mochila, resolver el problema de la mochila resuelve mi problema
import problema_mochila
def carlitos(c_publicitaria, P):
    return problema_mochila.mochila(c_publicitaria,P)




# Complejidad temporal: pseudopolinomial : O(n x W) = O(n x 2^m)donde  n representa la longitud de lecturas de los vectores de elementos del problema de la mochila
# y m representa la longitud en bits del valor de W
# W = 2^m

# No da lo mismo la moneda en nuestro sistema monetario argentino 100 dolares equivale por ejemplo a 100000 un valor con longitud muy grande en bits 
# lo que hace mas lento el algoritmo

