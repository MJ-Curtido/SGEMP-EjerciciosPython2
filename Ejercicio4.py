def letrasMayus(cadena):
    cont = 0

    for letra in cadena:
        if letra > 'A' and letra < 'Z':
            cont += 1

    return cont

print("Introduzca una palabra")
palabra = input()
print(letrasMayus(palabra))