""" Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a
comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] 
contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, 
las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. Implementar un algoritmo que, 
por backtracking, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que 
dejan la menor cantidad de espacios vacíos). """

def max_grupos_bodegon(P, W):
    max_conjunto_grupos = []
    _max_grupos_bodegon_rec(P,W,0,max_conjunto_grupos,[])
    return max_conjunto_grupos

def _max_grupos_bodegon_rec(P,W,indice_grupo,max_conjunto_grupos,conjunto_grupos_actual):
    suma_conjunto_grupos_actual = sum(conjunto_grupos_actual)
    suma_max_conjunto_grupos = sum(max_conjunto_grupos)
    if indice_grupo == len(P):
        if suma_conjunto_grupos_actual > suma_max_conjunto_grupos and suma_conjunto_grupos_actual <= W:
            max_conjunto_grupos.clear()
            max_conjunto_grupos.extend(conjunto_grupos_actual)    
        return
    
    if suma_conjunto_grupos_actual > suma_max_conjunto_grupos and suma_conjunto_grupos_actual <= W:
        max_conjunto_grupos.clear()
        max_conjunto_grupos.extend(conjunto_grupos_actual)
    if suma_conjunto_grupos_actual > W:
        return
    
    conjunto_grupos_actual.append(P[indice_grupo])
    _max_grupos_bodegon_rec(P,W,indice_grupo+1,max_conjunto_grupos,conjunto_grupos_actual)
    conjunto_grupos_actual.pop()
    _max_grupos_bodegon_rec(P,W,indice_grupo+1,max_conjunto_grupos,conjunto_grupos_actual)

    return