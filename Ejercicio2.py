def masLarga(lista):
    cadena = ""

    for elem in lista:
        if len(elem) > len(cadena):
            cadena = elem

    return cadena

print(masLarga(["manuel", "miguelito", "supercalifragilisticoespialidoso", "martuki"]))