from functools import reduce

def cuenta(operacion, *args, **kwargs):
    resul = 0
    if operacion == 'suma':
        for i in args:
            resul += i
    else:
        resul = reduce((lambda x, y: x*y),args)
    print('el resultado es ' + str(resul))
    for clave,valor in kwargs.items():
        print('{} del solicitante es {}'.format(clave,valor))


cuenta('multiplicacion',2,2,nombre = 'anabel', apellido = 'plv', direccion = '120 n 538')