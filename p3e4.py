anim={'Gato Montes':2,'Yacare overo':4,'Boa acuática':5}

for animal,pos in anim.items():
    print(' _ '* len(animal[0:pos]) + animal[pos] + ' _ ' * len(animal [pos + 1:len(animal)]))