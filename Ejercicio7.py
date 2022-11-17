cont = 1
lista = []
contMay20 = 0

while cont <=10:
    print(f"Inserte la edad de la persona {cont}")
    edad = input()

    lista.append(edad)

    cont += 1

for edad in lista:
    if int(edad) > 20:
        contMay20 += 1

print(contMay20)