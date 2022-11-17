lista = ["Paula", "Manu", "Andrea", "Miguelito", "Marta", "Nathan", "Callie", "Bustamante", "Jager"]

cont = 0
letra = "p"

while not letra.__eq__("*"):
    cont = 0

    print("Inserte una letra (* si quieres parar)")
    letra = input()

    if not letra.__eq__("*"):
        for elem in lista:
            if elem[0].casefold().__eq__(letra.casefold()):
                cont += 1

        print(cont, "\n")