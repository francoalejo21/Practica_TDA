"""Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que
usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que
construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de R kilómetros (valor constante
conocido). Implementar un algoritmo Greedy que reciba las ubicaciones de las casas (número de kilómetro sobre esta
ruta) y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura,
y se construya para esto la menor cantidad de antenas posibles. Indicar y justificar la complejidad del algoritmo
implementado. Justificar por qué se trata de un algoritmo greedy."""

def ruta(kilometros, K, R):
    casas = sorted(kilometros)
    antenas = []
    for casa in casas:
        if antenas == []:
            antenas.append(casa+R) if casa+R <=K else antenas.append(K)
            continue
        ultima_antena = antenas[-1]
        if ultima_antena + R < casa:
            antenas.append(casa + R) if casa+R <=K else antenas.append(K)
    return antenas

if __name__ == "__main__":
    
    # Ejemplo
    kilometros = [1, 2, 5, 6, 9, 11, 13]
    K = 17
    R = 2
    print(ruta(kilometros,K,R))