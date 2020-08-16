import random

colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
palabras = [('grave',['molesto']), ('aguda',['ratón']),('esdrujula',['murciélago'])]
dic={}

def cargar():
    for i in coordenadas:
        dic[i]=colores[random.randrange(len(colores))]
    print(dic)

def imprimirA ():
    num1=random.randrange(500)
    num2=random.randrange(500)
    print('¿Cuanto es la suma entre ',num1,' y ',num2,'?')
    resul=int(input())
    num1+=num2
    if (resul == num1):
        print('Excelente!, ese es el resultado')
    else:
            print('mmm No! te equivocaste, el resultado era ',num1)

def imprimirB ():
    num=random.randrange(len(palabras))
    pal=palabras[num][1]
    print(pal)
    resul=input('¿Que tipo de palabra cree que es por su acentuacion? (GRAVE-AGUDA-ESDRUJULA) ').lower()
    if (resul == palabras[num][0]):
        print('Asi es! la palabra ',pal,' es de tipo ',palabras[num][0])
    else:
        print('Claro que   NO!, La palabra ',pal,' es de tipo', palabras[num][0], ', estudia mas para la proxima. . .')

funciones = {'azul': imprimirA,'amarillo': imprimirB,'rojo': imprimirA, 'blanco': imprimirB,'negro':imprimirA}

def jugar():
    coor=(input('ingrese la cordenada separada por coma '))
    x,y = coor.split(',')
    funciones[dic[(int(x),int(y))]]()


cargar()
jugar()