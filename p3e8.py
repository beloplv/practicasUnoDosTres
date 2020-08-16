def suma (*args):
    suma=0
    for i in args:
        suma += i
    return suma

def imprimir (**kwargs):
    for clave, valor in kwargs.items():
        print("Su {} es {}".format(clave, valor))

print(suma(10,10,10,10,10,10,10))
imprimir(nombre = 'anabel',sexo ='femenino' )