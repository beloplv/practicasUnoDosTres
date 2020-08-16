frase = '''Si trabajás mucho CON computadoras, eventualmente encontrarás
que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear 
realizar una búsqueda y reemplazo en un gran número DE archivos de
texto, o renombrar y reorganizar un montón de archivos con fotos de una
manera compleja. Tal vez quieras escribir alguna pequeña base de datos
personalizada, o una aplicación especializada con interfaz gráfica,
o UN juego simple.'''

frase = frase.replace(',','').replace('.','').lower().split(' ')
frase =set(frase)
print (frase)

dic = {}

for i in frase:
    if len(i) in dic:
        dic[len(i)].append(i)
    else:
        dic[len(i)]= [i]

print(dic)