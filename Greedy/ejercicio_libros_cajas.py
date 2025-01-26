"""
    Idem al ejericio de las bolsas pero en vez de productos, libros y en vez de bolsas son cajas
"""

def cajas(capacidad, libros):
    libros = sorted(libros, reverse = True)
    cajas_abiertas = []
    for libro in libros:
        if len(cajas_abiertas) > 0 : 
            colocado = False
            for caja in cajas_abiertas:
                if sum(caja) + libro <= capacidad:
                    caja.append(libro)
                    colocado = True
                    break
            if not colocado:
                nueva_caja = []
                nueva_caja.append(libro)
                cajas_abiertas.append(nueva_caja)
                
        else:
            nueva_caja = []
            nueva_caja.append(libro)
            cajas_abiertas.append(nueva_caja)
    return cajas_abiertas

libros = [1,5,2,5,2,4,5,2]
capacidad =5
print(cajas(capacidad,libros))