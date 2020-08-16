dic={'anabel':{'nivel':4,'puntaje':5000,'tiempo':78},'daiana':{'nivel':54,'puntaje':45870,'tiempo':888},'hernan':{'nivel':1,'puntaje':50,'tiempo':8}}

def modificar():
    print('modificar')
    nom = input('ingrese el nombre del jugador ')
    nivel = input('ingrese el nivel ')
    pun = input ('ingrese el puntaje ')
    ti = input ('ingrese el tiempo ')
    if nom in dic.keys():
        if pun > dic[nom]['puntaje']:
            dic[nom] = {'nivel':nivel,'puntaje':pun,'tiempo':ti}
        else:
            print('El puntaje no es mayor entonces no se hace la modificacion')
    else:
        print('No existe ese jugador')

def agregar(dic):        
    nom = input('ingrese el nombre del jugador -> para terminar ingresar (zzz) ')
    while nom != 'zzz':
        nivel = input('ingrese el nivel ')
        pun = input ('ingrese el puntaje ')
        ti = input ('ingrese el tiempo ')
        dic[nom] = {'nivel':nivel,'puntaje':pun,'tiempo':ti}
        nom = input('ingrese el nombre del jugador -para terminar ingresar (zzz) ')

def buscar():
    nom = input('ingrese el nombre del usuario a buscar ')
    if nom in dic.keys():
        print(dic[nom])
    else:
        print('no existe')

def imprimir():
    print('nombres de los usuarios')
    print(dic.keys())
    print('Ranking top 10')
    juga = sorted(dic.items(),key=lambda jugador: jugador[1]['puntaje'],reverse=True)
    print(juga[:10])

def maximo():
    print('Jugador que obtuvo mayor puntaje')
    print(max(dic.items(),key=lambda jugador:jugador[1]['puntaje']))

agregar(dic)
modificar()
buscar()
maximo()
imprimir()