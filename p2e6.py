print('ingrese dos numeros')
num1 = int(input('numero 1: '))
num2 = int(input('numero 2: '))
print ('Menú de opciones :')
print('1: suma')
print('2: resta')
print('3: multiplicacion')
print('4: division')
print('0: para terminar')
aux = int(input())
resul = 0
if aux != 0:
    if aux == 1:
        resul = num1 + num2
    elif aux == 2:
        resul = num1 - num2
    elif aux == 3:
        resul = num1 * num2    
    elif aux == 4:
        resul = num1 / num2
    print('Resultado ' + str(resul))