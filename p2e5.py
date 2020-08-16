print ('Menú de opciones para la lista de números a ingresar:')
print('1: ingresar números')
print('2: ordenar números')
print('3: calcular el máximo')
print('4: calcular el mínimo')
print('5: calcular el promedio')
print('0: para terminar')
num = int(input())

lista = []
while num != 0:
    if num == 1:
        print('-1 para terminar')
        aux = int(input('numero: '))
        while aux != -1:
            lista.append(aux)
            print('-1 para terminar')
            aux = int(input('numero: '))
    if len(lista) != 0:
        if num == 2:
            print('ordenado')
            lista.sort()
            print(lista)
        elif num == 3:
            print('maximo')
            print(max(lista))
        elif num == 4:
            print('minimo')
            print(min(lista))
        elif num == 5:
            print('promedio')
            print (sum(lista)/len(lista))
    else:
        print('Lista vacia') 
    print ('Menú de opciones para la lista de números a ingresar:')
    print('1: ingresar números')
    print('2: ordenar números')
    print('3: calcular el máximo')
    print('4: calcular el mínimo')
    print('5: calcular el promedio')
    print('0: para terminar')
    num = int(input())        
    