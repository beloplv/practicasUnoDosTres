tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

lista1=[]
lista2=[]

num = int(input('ingrese un numero '))

for i in tam:
    im,space,tupla = i.partition(' ')
    aux = (int(tupla.split(',')[0]), int(tupla.split(',')[1]))
    if num >= aux[0]:
        lista1.extend([im,tupla])
    else:
        lista2.extend([im,tupla])

print(lista1)
print(lista2)

