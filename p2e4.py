import random

preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], ['Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no']]
puntaje = 0
aux=len(preguntas)-1
print(aux)
while len(preguntas) >= 1:
    num = random.randint(0,aux)
    res= input(preguntas[num][0]).lower()
    if res == preguntas[num][1]:
        puntaje += 1
        print('Excelente suma un punto')
    else:
        print('ERROR')
    del preguntas[num]
    aux -= 1

print('Puntos totales '+ str(puntaje))


