'''
Se necesita obtener información sobre un texto y obtener información de cada palabra del mismo.
Para obtener la información requerida se solicita que se realicen
5(cinco) funciones: calcular_caracteres_unicos(), gen_informacion(), ordenar_informacion(),
calcular_max_palabra() y calcular_min_palabra().

la función:
calcular_caracteres_unicos()
Recibe un string  y retorna una lista con los caracteres que aparecen una única vez en el string.
Ejemplo:
calcular_caracteres_unico("CASA") devuelve ["C","S"] dado que aparecen una sola vez en el string "CASA"

La función:
gen_informacion()
Recibe una lista de strings y retorna una lista de tuplas con la cantidad de caracteres únicos del string y el string en mayúscula,
 se debe utilizar la función calcular_caracteres_unicos().
Ejemplo:
gen_informacion(["CASA","gato"]) devuelve [(2,"CASA"),(4,"GATO")]

La función:
ordenar_informacion()
Recibe una lista de datos procesados (generados por la función gen_informacion) y un criterio de ordenamiento:
Si el Criterio es igual a "cantidad" se debe retornar la lista ordenada por el valor numérico.
Si el Criterio es igual a "palabra" se debe retornar la lista ordenada por la palabra alfabéticamente.
Si se ingresa cualquier otra cosa, se debe imprimir "No se ingresó un criterio válido" y se debe terminar 
obligatoriamente la ejecución de todo el programa.

La función:
calcular_max_palabra()
Recibe una lista de datos procesados(generados por la función gen_informacion) y retorna la tupla con la palabra con la mayor cantidad de caracteres únicos.

La función:
calcular_min_palabra()
Recibe una lista de datos procesados(generados por la función  gen_informacion) y retorna la tupla con la menor cantidad de caracteres únicos.
'''

import sys
def calcular_caracteres_unicos(palabra):
    lista = []
    for i in palabra:
        if palabra.count(i) == 1:
            lista.append(i)
    return lista

def gen_informacion(lista):
    lista2 = []
    for i in lista:
        lis = calcular_caracteres_unicos(i)
        lista2.append((len(lis),i.upper()))
    return lista2

def ordenar_informacion(lista, criterio):
    if criterio == 'cantidad':
        lista = sorted(lista, key = lambda jug: jug[0])
    elif criterio == 'palabra':
        lista = sorted(lista, key = lambda jug: jug[1])
    else:
        print('no se ingreso un criterio valido')
        sys.exit()
    return lista

def calcular_max_palabra(lista):
    return max(lista, key = lambda jug: jug[0])

def calcular_min_palabra(lista):
    return min(lista , key = lambda jug: jug[0])


lista = ['casa','gato','perro','multifactorial','casanova','annabell','pato']
info = gen_informacion(lista)
print(info)
print(ordenar_informacion(info,'palabra'))
print('minimo')
print(calcular_min_palabra(info))
print('maximo')
print(calcular_max_palabra(info))