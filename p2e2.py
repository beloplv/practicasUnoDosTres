tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

lista = []

for i in tam:
    im,space,tupla = i.partition(' ')
    aux= (int(tupla.split(',')[0]),int(tupla.split(',')[1]))
    lista.extend([aux])

lista.sort()
print(lista)


