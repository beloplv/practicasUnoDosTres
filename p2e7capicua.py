def es_capicua(num):
    capicua = False
    numero_al_reves = num[::-1]
    if num == numero_al_reves:
        capicua = True
    return capicua