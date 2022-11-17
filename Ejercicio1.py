def maxInList(lista):
    lista.sort()

    return lista[len(lista) - 1]

print(maxInList([0, 5, -9, 17, -90]))