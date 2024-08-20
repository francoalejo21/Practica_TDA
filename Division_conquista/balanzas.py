def balanza(joyas_izq, joyas_der):
    suma_izq = 0
    suma_der = 0
    for joya in joyas_izq:
        suma_izq+=joya
    for joya in joyas_der:
        suma_der+=joya
    if suma_izq == suma_der:
        return 0
    if suma_izq > suma_der:
        return 1
    if suma_izq < suma_der:
        return -1
