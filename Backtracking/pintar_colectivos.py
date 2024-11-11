""" Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una misma 
parada de colectivo nunca pararán dos colectivos que usen el mismo color. El problema es que ya saben que eso está sucediendo hoy 
en día, así que van a repintar todas las líneas de colectivos. Por problemas presupuestarios, desean pintar los colectivos con la
menor cantidad posible k colores diferentes. Como no quieren parecer un grupo de improvisados que malgasta los fondos públicos, 
quieren hacer un análisis para saber cuál es ese mínimovalor para cumplir con lo pedido (pintar cada línea con alguno de los k 
colores, de tal forma que no hayan dos de mismo color coincidiendo en la misma parada). Considerando que se tiene la información 
de todas las paradas de colectivo y qué líneas paran allí, modelar el problema utilizando grafos e implementar un algoritmo que 
determine el mínimo valor k para resolver el problema. Indicar la complejidad del algoritmo implementado.
Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe. """

"""
def pintar_colectivos(colectivos, paradas):
    cantidad_colores_asignados = [len(colectivos)]
    _pintar_colectivos_rec(colectivos, 0, {}, paradas, cantidad_colores_asignados)
    return cantidad_colores_asignados
    
def _pintar_colectivos_rec(colectivos, indice_colectivo, colores_asignados, paradas, cantidad_colores_asignados):
    if indice_colectivo == len(colectivos):
        if colectivos_pintados(colectivos, colores_asignados) and hay_colectivos_mismo_color_en_parada(colores_asignados, paradas) and len(colores_asignados) < cantidad_colores_asignados[0]:
            cantidad_colores_asignados.clear()
            cantidad_colores_asignados.extend(len(colores_asignados))
        return
    if colectivos_pintados(colectivos, colores_asignados) and hay_colectivos_mismo_color_en_parada(colores_asignados, paradas) and len(colores_asignados) < cantidad_colores_asignados[0]:
        cantidad_colores_asignados.clear()
        cantidad_colores_asignados.extend(len(colores_asignados))
        return
    for color in range(len(colectivos)): #como máximo podemos pintar con un color cada colectivo en el peor caso
        #pruebo pintando el colectivo
        colores_asignados[colectivos[indice_colectivo]] = color
        print(colores_asignados)
        _pintar_colectivos_rec(colectivos, indice_colectivo + 1, colores_asignados, paradas, cantidad_colores_asignados)
        #pruebo despintando el colectivo
        colores_asignados.pop(colectivos[indice_colectivo])
        _pintar_colectivos_rec(colectivos, indice_colectivo + 1, colores_asignados, paradas,cantidad_colores_asignados)

def colectivos_pintados(colectivos, colores_asignados):
    return len(colectivos) == len(colores_asignados)

def hay_colectivos_mismo_color_en_parada(colores_asignados, paradas):
    for parada in paradas:
        for colectivo in parada:
            color = colores_asignados[colectivo]
            for colectivo_adyacente in parada:
                if colectivo_adyacente == colectivo:
                    continue
                if colores_asignados[colectivo_adyacente] == color:
                    return False
    return True

colectivos = [7,50,101,21]
paradas = [[7,50,21],[50,101]]
print(pintar_colectivos(colectivos,paradas))    
 """

def pintar_colectivos(colectivos, paradas):
    # Inicializamos con la cantidad máxima de colores (uno para cada colectivo).
    cantidad_colores_minima = [len(colectivos)]
    _pintar_colectivos_rec(colectivos, 0, {}, paradas, cantidad_colores_minima)
    return cantidad_colores_minima[0]

def _pintar_colectivos_rec(colectivos, indice_colectivo, colores_asignados, paradas, cantidad_colores_minima):
    # Si hemos asignado colores a todos los colectivos, verificamos si la solución actual es la óptima.
    if indice_colectivo == len(colectivos):
        colores_usados = len(set(colores_asignados.values()))
        if colores_usados < cantidad_colores_minima[0]:
            cantidad_colores_minima[0] = colores_usados
        return
    
    colectivo_actual = colectivos[indice_colectivo]
    
    # Intentamos asignar cada color posible hasta el límite actual de colores mínimos encontrados
    for color in range(cantidad_colores_minima[0]):
        # Verificamos que el color sea válido en base a las paradas
        if es_color_valido(colectivo_actual, color, colores_asignados, paradas):
            colores_asignados[colectivo_actual] = color
            _pintar_colectivos_rec(colectivos, indice_colectivo + 1, colores_asignados, paradas, cantidad_colores_minima)
            # Eliminamos la asignación para probar otras combinaciones
            del colores_asignados[colectivo_actual]

def es_color_valido(colectivo, color, colores_asignados, paradas):
    # Recorremos cada parada y verificamos si el colectivo actual comparte parada con algún otro colectivo pintado del mismo color
    for parada in paradas:
        if colectivo in parada:
            for otro_colectivo in parada:
                if otro_colectivo != colectivo and colores_asignados.get(otro_colectivo) == color:
                    return False
    return True

# Ejemplo de uso
colectivos = [7, 50, 101, 21]
paradas = [[7, 50, 21], [50, 101]]
print(pintar_colectivos(colectivos, paradas))