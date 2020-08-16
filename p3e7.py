dic={'paez':{'nivel':7,'puntaje':88,'tiempo':8},'bartolome':{'nivel':17,'puntaje':78,'tiempo':4},'cadaa':{'nivel':54,'puntaje':50,'tiempo':77},'ruffolo':{'nivel':63,'puntaje':74,'tiempo':4},'bortolotto':{'nivel':70,'puntaje':20,'tiempo':10},'lopez':{'nivel':70,'puntaje':880,'tiempo':40}}

print('maximos 10')
juga = sorted(dic.items(), key = lambda jugador: jugador[1]['puntaje'],reverse = True)
print(juga[:10])
print('ordenados por apellido')
juga = sorted(dic.keys(), key = lambda jugador: jugador[0] )
print(juga)
print('ordenados por el nivel alcanzado')
juga = sorted(dic.items(), key = lambda jugador: jugador[1]['nivel'],reverse = True)
print(juga)