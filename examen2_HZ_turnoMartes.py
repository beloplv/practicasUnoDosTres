'''El objetivo es implementar algunas funciones necesarias para desarrollar un juego de cartas.

Primeramente se pide implementar dos funciones para comenzar un juego:

armar_mazo
Esta función debe recibir una lista de palos (en formato string cada uno) y una lista de valores(valores enteros).
La misma debe retornar una estructura que represente un mazo de cartas donde cada carta debe ser una tupla compuesta
por (palo, valor).

armar_mano
Esta función arma una mano para un juego. Realiza la mezcla de las cartas y las reparte a los jugadores. 
La función debe recibir un mazo, una lista de jugadores y la cantidad de cartas a repartir por jugador. 
Las cartas se deben repartir de forma aleatoria, pero no se deben repetir cartas entre los jugadores 
en una misma mano. La estructura que se retorne debe brindar la posibilidad de acceder a la mano que 
le tocó directamente con el nombre del jugador.

Con estas dos funciones se permite armar un mazo de cartas disponible para jugar. Para poder implementar 
el juego se solicita dos funciones:

mayor_valor
Recibe la una mano y debe calcular el jugador que más  puntos tiene al sumar los valores de sus cartas 
indpendientemente de los palos. Se debe devolver una tupla con el nombre del jugador y el puntaje que sumó.

repite_palo
Esta función recibe una mano y retorna para cada jugador si tiene o no palos repetidos entre las cartas 
que le tocaron. La estructura que retorne debe ser fácil de accederse teniendo el nombe del jugador para 
el que quiero saber el resultado.'''
import random

def armar_mazo(palos,valor):
    mazo=[]
    for i in valor:
        for x in palos:
            mazo.append((x,int(i)))
    return mazo

def armar_mano(mazo,jugadores,cantidad):
    mano = {}
    for i in jugadores:
        random.shuffle(mazo)
        listacartas = []
        for x in range(cantidad):
            listacartas.append(mazo[x])
        mano[i] = listacartas
    return mano

def mayor_valor(mano):
    nom = ''
    maximo = 0
    for i in mano.keys():
        total =	sum(e[1] for e in mano[i])
        if total > maximo:
            maximo = total
            nom = i
    return (nom,maximo)

def repite_palo(mano):
    repetidos = {}
    ok = False
    for key,valor in mano.items():
        lista = []
        for i in valor:
            lista.append(i[0])
        lista = set(lista)
        if len(valor) > len(lista):
            repetidos[key] = 'tiene repetidos'
            ok = True
        if not ok:
            repetidos[key] = 'no tiene repetidos'
    return repetidos

palos = ['copa','oro','basto','espada']
valor = ['1','2','3','4','5','6','7','8','9','10','11','12']
jugadores = ['anabel','hernan','daiana','silvia','carlos']
mazo = armar_mazo(palos,valor)
mano = armar_mano(mazo,jugadores,4)
print('maximo puntaje')
print(mayor_valor(mano))
print('repiten palos')
print(repite_palo(mano))

        
