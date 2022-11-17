print("Inserte el año de curso")
anyoCurso = input()
cont = 1
lista = []

while cont <= 3:
    print(f"Inserte el nombre de la persona {cont}")
    nombre = input()

    print(f"Inserte el año de nacimiento de la persona {cont}")
    anyoNac = input()

    lista.append((nombre, anyoNac))

    cont += 1

cont = 0
while cont < len(lista):
    print(f"{lista[cont][0]} cumplirá durante el año del curso {int(anyoCurso) - int(lista[cont][1])} años")
    cont += 1