import random

colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]


def asociar_colores_repetidos():
    dic = {}
    for i in coordenadas:
        pos = random.randint(0,len(colores)-1)
        dic[i] = colores[pos]
    return dic

def asociar_colores_sin_repetidos():
    dic = {}
    for i in coordenadas:
        pos = random.randint(0,len(colores)-1)
        dic[i] = colores[pos]
        del colores[pos]
    return dic

def sumar_numeros():
    num1 = random.randrange(100)
    num2 = random.randrange(300)
    suma = num1 + num2
    res = int (input('ingrese el resultado de la suma: '+ str(num1) + ' + '+  str(num2) + '='))
    if res == suma:
        print('Excelente, respondiste bien')
    else:
        print('Error. respondiste mal')

def palabras():
    palabras = [('grave',['molesto']), ('aguda',['ratón']),('esdrujula',['murciélago'])]
    pos = random.randint(0,len(palabras)-1)
    print('ingrese que tipo de palabra es ')
    print(palabras[pos][1])
    res = input()
    if res == palabras[pos][0]:
        print('Excelente, respondiste bien')
    else:
        print('Error. respondiste mal')


#print(asociar_colores_repetidos())
def jugar():
    dic = asociar_colores_sin_repetidos()  
    print(coordenadas)
    res = input('ingrese la coordenada separada por una coma ')
    funciones = {'azul': sumar_numeros(), 'amarillo':palabras(), 'rojo':sumar_numeros(), 'blanco':palabras(), 'negro':sumar_numeros()} 
    funciones[dic['('+int(res)+')']]()
    print('h')

jugar()
