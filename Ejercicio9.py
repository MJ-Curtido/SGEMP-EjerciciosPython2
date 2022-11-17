def contarVocales(palabra):
    contA = 0
    contE = 0
    contI = 0
    contO = 0
    contU = 0

    for letra in palabra:
        if letra.casefold().__eq__("a"):
            contA += 1
        else:
            if letra.casefold().__eq__("e"):
                contE += 1
            else:
                if letra.casefold().__eq__("i"):
                    contI += 1
                else:
                    if letra.casefold().__eq__("o"):
                        contO += 1
                    else:
                        if letra.casefold().__eq__("u"):
                            contU += 1

    print(f"Tiene ->\n\ta= {contA}\n\te= {contE}\n\ti= {contI}\n\to= {contO}\n\tu= {contU}")

palabra = "Paca"

while not palabra.__eq__("*"):
    print("Inserte una palabra (* para terminar):")
    palabra = input()

    if not palabra.__eq__("*"):
        contarVocales(palabra)