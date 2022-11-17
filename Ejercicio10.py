def esBisiesto(anyo):
    if anyo % 4 == 0 and anyo % 100 != 0 or anyo % 400 == 0:
        return True
    else:
        return False

anyo = "0"

while not anyo.__eq__("*"):
    print("Inserte un año (* para terminar):")
    anyo = input()

    if not anyo.__eq__("*"):
        print(esBisiesto(int(anyo)))