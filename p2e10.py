imagenes=['im1','im2','im3']

dic={}
x=0
y=0
while len(imagenes) != 0: 
    x = int(input('ingrese la coordenada x '))
    y = int(input('ingrese la coordenada y '))
    if (x,y) in dic.values():
         print('esa coordenada ya existe, pruebe devuelta')
    else:
        dic[imagenes[0]]=(x,y)
        del imagenes[0]
    
        


print(dic)