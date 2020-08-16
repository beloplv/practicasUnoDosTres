frase = "Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número de archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o un juego simple."
frase = frase.lower().split(' ')
string = (str (input ('ingrese un string ')))

nuevo = (' '.join(frase))
lista_coincidencias = [palabra for palabra in frase if string in palabra]

print(len(lista_coincidencias))
print(nuevo)