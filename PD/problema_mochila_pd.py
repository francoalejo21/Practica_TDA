IDX_VALOR = 0
IDX_PESO = 1


def mochila_pd(elementos, W):
    matriz = [[0 for j in range(W + 1)] for i in range(len(elementos) + 1)]
    for i in range(1, len(elementos) + 1):
        elem = elementos[i-1]
        for j in range(1, W + 1):
            if elem[IDX_PESO] > j:
                matriz[i][j] = matriz[i-1][j]
            else:
                matriz[i][j] = max(matriz[i-1][j], matriz[i-1][j - elem[IDX_PESO]] + elem[IDX_VALOR])
    return matriz[len(elementos)][W]
elementos = [[58,7],
[15, 6],
[51, 12],
[31, 2],
[13, 12],
[89, 15],
[19, 9],
[4, 12],
[75, 8],
[50,8]]


def ordenar_por_mayor_valor(elementos):
    return sorted(elementos, key=lambda e: e[IDX_VALOR], reverse=True)


def ordenar_por_menor_peso(elementos):
    return sorted(elementos, key=lambda e: e[IDX_PESO])


def ordenar_por_mayor_relacion_valor_peso(elementos):
    return sorted(elementos, key=lambda e: e[IDX_VALOR]/e[IDX_PESO], reverse=True)


def mochila_greedy(elementos, W, ordenamiento):
    elementos_ord = ordenamiento(elementos)
    capacidad_usada = 0
    valor_obtenido = 0
    for elem in elementos_ord:
        if elem[IDX_PESO] + capacidad_usada > W:
            continue
        capacidad_usada += elem[IDX_PESO]
        valor_obtenido += elem[IDX_VALOR]
    return valor_obtenido

print(mochila_pd(elementos,15))