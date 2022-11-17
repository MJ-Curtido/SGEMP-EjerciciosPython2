import math

def convierteEnteroABin(num):
    cadena = ""

    while num >= 2:
        cadena += f"{math.trunc(num % 2)}"

        num = num / 2

    if (num / 2) > 0:
        cadena += f"{1}"
    else:
        cadena += f"{0}"

    return cadena

print(convierteEnteroABin(89))

def convierteBinAEntero(binario):
    num = 0
    cont = 0
    binario = binario[::-1]

    for elem in binario:
        if elem == "1":
            num += 2 ** cont

        cont += 1

    return num

print(convierteBinAEntero("1001101"))