'''Te daban un string con números, el que daban ellos como ejemplo era "111 4334 334 4 5 773".
A partir de eso tenías que terminar devolviendo:
{111: {'es_capicua': True, 'suma_es_primo': True}, 4334: {'es_capicua': True, 'suma_es_primo': False},
334: {'es_capicua': False, 'suma_es_primo': False}, 773: {'es_capicua': False, 'suma_es_primo': True}}
del string con números, tenías que considerar solamente los números que son colegas (los números que 
tienen dígitos repetidos, por ejemplo, 11 lo es, pero 12 no) suma_es_primo, era saber si la suma de 
los dígitos era primo o no (esto se me hizo que lo hicimos en alguna práctica pero no lo encontré)
esa es la función que ellos no daban inicialmente en la estructura y yo la creé... 
dentro de esa función llamaba a es_primo y validaba si la suma de los dígitos es primo o no
y bueno, lo de es_capicua también habíamos hecho lo mismo en una práctica para saber si era palíndromo 
o no, al tener al número como string, sería lo mismo'''

string = '111 4334 334 4 5 773 845'
def es_colega(num):
    colega = False
    #if len(num) > 1:
    numero= set(i for i in num if num.count(i) > 1)
    if len(numero) > 0:
        colega = True
    print(numero)
    return colega

def es_capicua(num):
    capicua = False
    numero_al_reves = num[::-1]
    if num == numero_al_reves:
        capicua = True
    return capicua

def es_primo(num):
    if int(num) <= 1:
        return False
    else:
        for x in range(2,num):
            if num % x == 0 and 1 != num:
                return False
        return True

def suma_es_primo(num):
    suma = 0
    for cifra in num:
        suma += int(cifra)
    return es_primo(suma)

def cargar(string):
    dic = {}
    lista = string.split(' ')
    for i in lista:
        if es_colega(i):
            dic[i] = {'es_capicua':es_capicua(i),'suma_es_primo':suma_es_primo(i)}
    return dic

print(cargar(string))

