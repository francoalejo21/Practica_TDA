""" Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. 
Implementar un algoritmo que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden 
luminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), 
y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”).

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se 
describe """

# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos
import time
casilleros_alcance = [(dy, dx) for dy in range(-2, 3) for dx in range(-2, 3)]
def calcular_casilleros_iluminados(faros, matriz):
    casilleros_iluminados = set()
    for y, x in faros:
        for dy, dx in casilleros_alcance:
            nuevo_y, nuevo_x = y + dy, x + dx
            if 0 <= nuevo_y < len(matriz) and 0 <= nuevo_x < len(matriz[0]):
                casilleros_iluminados.add((nuevo_y, nuevo_x))
    return casilleros_iluminados

def estan_todos_iluminados(submarinos, casilleros_iluminados):
    return submarinos.issubset(casilleros_iluminados)

def backtrack_optimizado(submarinos, matriz, faros, mejor_solucion, candidatos, index):
    # Poda: Si los faros actuales ya son más que la mejor solución conocida
    if len(faros) >= len(mejor_solucion):
        return

    # Si todos los submarinos están iluminados
    if estan_todos_iluminados(submarinos, calcular_casilleros_iluminados(faros, matriz)):
        if len(faros) < len(mejor_solucion):
            mejor_solucion.clear()
            mejor_solucion.update(faros)
        return

    # Explorar los candidatos restantes
    for i in range(index, len(candidatos)):
        y, x = candidatos[i]
        if ilumina_mas_submarinos(y, x, faros, matriz, submarinos):
            faros.add((y, x))
            backtrack_optimizado(submarinos, matriz, faros, mejor_solucion, candidatos, i + 1)
            faros.remove((y, x)) 
    
def ilumina_mas_submarinos(y, x, faros, matriz, submarinos):
    if len(faros) == 0: # si no hay faros iluminados
        #print("No habia faros entonces todo bien que devuelva True")
        return True
    casilleros_iluminados = calcular_casilleros_iluminados(faros, matriz)
    nuevo_faro = (y, x)
    nuevos_faros = set()
    nuevos_faros.add(nuevo_faro)
    nuevos_casilleros_iluminados = calcular_casilleros_iluminados(nuevos_faros, matriz)
    for casillero  in nuevos_casilleros_iluminados:
        if casillero in submarinos:
            if casillero not in casilleros_iluminados:
                return True

    return False
    

def submarinos(matriz):
    # Identificar todas las posiciones de submarinos
    submarinos = {(i, j) for i, row in enumerate(matriz) for j, val in enumerate(row) if val}
    if not submarinos:
        return []

    # Generar candidatos ordenados por densidad de submarinos en el radio
    candidatos = sorted(
        [(i, j) for i in range(len(matriz)) for j in range(len(matriz[0]))],
        key=lambda pos: sum((i, j) in submarinos for i, j in calcular_casilleros_iluminados({pos}, matriz)),
        reverse=True
    )
    # Inicializar variables
    faros = set()
    mejor_solucion = set(submarinos)  # Peor caso: un faro por submarino
    backtrack_optimizado(submarinos, matriz, faros, mejor_solucion, candidatos, 0)
    return list(mejor_solucion)

def main():
    matriz = [
        [True, False, False, True, False, False, False, False ],
        [False, False, False, False, False, False, False, False ],
        [False, False, False, False, False, False, False, False ],
        [False, True, False, True , False, False, False, False],
        [False, False, False, False , False, False, False, False],
        [False, False, False, True, False, False, False, False ],
        [False, True, False, False, False, False, False, True],
        [False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, True, False],
        [False, False, False, False, False, False, False, False],
        [False, False, True, False, False, False, False, False] 
    ]
    resultado = submarinos(matriz)
    print("Faros necesarios:", len(resultado))
    print("Posiciones de los faros:", resultado)

if __name__ == "__main__":
    main()