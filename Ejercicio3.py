def filtrar_palabras(lista, num):
    listaMasN = []

    for elem in lista:
        if len(elem) > num:
            listaMasN.append(elem)

    return listaMasN

for elem in filtrar_palabras(["puerto", "americano", "piel", "cuero"], 5):
    print(elem)