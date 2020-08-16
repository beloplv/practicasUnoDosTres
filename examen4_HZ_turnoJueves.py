'''Se necesita procesar un string que representa un código html y recolectar información sobre los botones.

Para procesar el html se deben definir las funciones contar_clase(), encontrar_boton() y procesar_botones().

La función:

procesar_boton()
Recibe como parámetro un string con información de un botón con las características asociadas en el siguiente 
formato:

<button type="button_next" class="navbar-next" data-toggle="collapse" data-target=".navHeaderNext">
y debe devolver un diccionario con las claves, o sea el valor antes del "=", en este caso:

type, class, data-toggle, data-target
Y como valor el dato correspondiente que tiene cada uno, o sea, el valor luego del signo "=".

La función:

encontrar_botones()
Recibe un string que representa código html que puede contener varios botones con diferentes valores 
asociados a sus características, todas las líneas que identifican los botones respetan el formato:

<button type="valor", class="valor",... >
</button>
Y debe devolver una lista con la información correspondiente a cada botón, la cual es generada por la 
función procesar_boton(). A cada elemento devuelto por la función se le dede agregar la clave "span"  con 
el valor True o False, dependiendo si se encuentra o no dentro del contenido de los tags del botón el siguiente tag:

<span class="sr-only">Toggle navigation</span>
Es decir en el siguiente caso se agregaría True:
  
  <button type="button_next" class="navbar-next" data-toggle="collapse" data-target=".navHeaderNext">
    <span class="sr-only">Toggle navigation</span>
  </button>

  La función:

contar_clase()
Recibe una lista como la generada en la función encontrar_botones() y un string que indica una clase, o sea, 
un valor asociado a la carcterística "class" en el código html a cada botón. Debe devolver la cantidad 
de botones existentes en la lista de dicha clase.

Ejemplo:

Dado el siguiente string:

html = 
<div class="navbar-header">
    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderCollapse">
        <span class="sr-only">Toggle navigation</span>
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-next" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-next" data-toggle="collapse" data-target=".navHeaderNext">
    <span class="sr-only">Toggle navigation</span>
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
</div>


La función contar_clase pasando la clase "navbar-toggle" devuelve 3.
La función encontrar_botones devolvería:
[{'type': 'button', 'class': 'navbar-toggle', 'data-toggle': 'collapse', 'data-target': '.navHeaderCollapse>', 
'spn': True}, 
{'type': 'button_next', 'class': 'navbar-next', 'data-toggle': 'collapse', 'data-target': '.navHeaderNext>', 
'spn': False},
{'type': 'button_next', 'class': 'navbar-next', 'data-toggle': 'collapse', 'data-target': '.navHeaderNext>', 
'spn': True}, 
{'type': 'button_next', 'class': 'navbar-toggle', 'data-toggle': 'collapse', 'data-target': '.navHeaderNext>', 
'spn': False}, 
{'type': 'button_next', 'class': 'navbar-toggle', 'data-toggle': 'collapse', 'data-target': '.navHeaderNext>', 
'spn': False}]'''

def procesar_boton(string):
    dic = {}
    string =  string.replace('<button','').replace('>','').replace('"','').replace("'",'').strip().split(' ')
    for i in string:
        x = i.split('=')
        dic[x[0]] = x[1]
    return dic

def encontrar_botones(string):
    lista = []
    string = string.replace('</div>','').replace('<div class="navbar-next">','').replace('<div class="navbar-header">','').strip().split('</button>')
    for i in string:
        if i != '':
            i = i.strip()
            i = i.replace('    ','').replace('         ','').split('\n')
            info = procesar_boton(i[0])
            if '<span class="sr-only">Toggle navigation</span>' in i:
                info['spn'] = 'True'
            else:
                info['spn'] = 'False'
            lista.append(info)
    return lista

def contar_clase(info,caracteristica):
    cant = 0
    for i in info:
        if i['class'] == caracteristica:
            cant+=1
    print('la caracteristica '+ caracteristica + ' aparece '+str(cant)+ ' veces')

string = '''<div class="navbar-header">
    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderCollapse">
        <span class="sr-only">Toggle navigation</span>
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-next" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-next" data-toggle="collapse" data-target=".navHeaderNext">
    <span class="sr-only">Toggle navigation</span>
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
</div>
<div class="navbar-next">
    <button type="button_next" class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderNext">
    </button>
</div>'''

lista =encontrar_botones(string)
print(lista)
carac = input('ingrese caracteristica a buscar ')
contar_clase(lista,carac)