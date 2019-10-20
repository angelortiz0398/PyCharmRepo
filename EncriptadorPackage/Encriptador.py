from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


def Encriptar(S, L):
    alfabeto = {" ": 10, "A": 11, "B": 12, "C": 13, "D": 14, "E": 15, "F": 16, "G": 17, "H": 18, "I": 19, "J": 20,
                "K": 21, "L": 22, "M": 23, "N": 24, "Ñ": 25, "O": 26, "P": 27, "Q": 28, "R": 29, "S": 30, "T": 31,
                "U": 32, "V": 33, "W": 34, "X": 35, "Y": 36, "Z": 37, "a": 38, "b": 39, "c": 40, "d": 41, "e": 42,
                "f": 43, "g": 44, "h": 45, "i": 46, "j": 47, "k": 48, "l": 49, "m": 50, "n": 51, "ñ": 52, "o": 53,
                "p": 54, "q": 55, "r": 56, "s": 57, "t": 58, "u": 59, "v": 60, "w": 61, "x": 62, "y": 63, "z": 64,
                "á": 65, "é": 66, "í": 67, "ó": 68, "ú": 69, "¡": 70, "!": 71, "¿": 72, "?": 73, "#": 74, "$": 75,
                "%": 76, "&": 77, "(": 78, ")": 79, "=": 80, "@": 81, "+": 82, "*": 83, "[": 84, "]": 85, "{": 86,
                "}": 87, "<": 88, ">": 89, ",": 90, ";": 91, ".": 92, ":": 93, "-": 94, "_": 95, "/": 96, "'": 97,
                "0": 98, "|": 99, "¬": 100, "º": 101, "~": 102, "€": 103, "ª": 104, "·": 105, "½": 107, "¨": 108,
                "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    cad = 0
    cadAux = 0
    res = 0
    for i in range(len(str(S))):
        if S[i] == '"':
            cad += 0
        else:
            cad += alfabeto.get(S[i])
    for j in range(len(str(L))):
        if L[j] == '"':
            cadAux += 0
        else:
            cadAux += alfabeto.get(L[i])
    res = int(cad) + int(cadAux) + S.count("a") - S.count("e") + S.count("i") - S.count("o") + S.count("u")
    return '{0:8b}'.format(res)


def DesEncriptar(Alfabeto, Cadena, Llave):
    return Cadena


def main():
    while True:
        Cadena = input("Escriba la cadena que desee encriptar: ")
        if Cadena == "":
            print("No se aceptan cadenas vacias, por favor vuelvala a escribir")
        else:
            break
    while True:
        Llave = input("Escriba su llave: ")
        if Llave == "":
            print("No se aceptan cadenas vacias, por favor vuelvala a escribir")
        else:
            break
    print("Su cadena codificada es: " + str(Encriptar(Cadena, Llave)))
    while True:
        while True:
            res = input("¿Desea desencriptar la cadena? Escriba Si o No con este formato => [S/N]: ")
            if res == "":
                print("Escriba si o no")
            else:
                break
        try:
            if res.upper() == "S":
                print("La cadena es: " + str(Cadena))
                print("Y la llave es: " + str(Llave))
                break
            elif res.upper() == "N":
                break
        except ValueError:
            print("Escriba solo 'S' o 'N'")
        print("Escriba solo 'S' o 'N'")
    Form, Window = uic.loadUiType("Encriptador.ui")
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
