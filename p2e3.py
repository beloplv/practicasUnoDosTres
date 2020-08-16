tam = ['Auto', '123', 'Viaje', '50', '120']


lista = []

for i in tam:
    if i.isdecimal():
        lista.append(int(i))

lista.sort()
print(lista)


