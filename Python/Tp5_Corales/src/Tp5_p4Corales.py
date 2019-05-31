"""Las unicas cadenas que se admiten son las que no tienen numeros"""
import sys


def inputs(var):
    """Se encarga de ejecutar un input cada vez que se la llama
    siendo ejecutada desde el mismo archivo. En caso de que el
    programa sea ejecutado por otro archivo, devuelve la misma
    variable que se le ingresa"""
    if __name__ == "__main__":
        var = input()
        return var
    else:
        return var

import sys


def loop_preguntar_palabra(pal):
    """Itera la función preguntar_palabra hasta
    que las dos palabras introducidas sean validas.
    Luego ejecuta proceso_palabra"""
    while True:
        pal = preguntar_palabra(pal)
        if pal[0] == "Error":
            continue
        else:
            proceso_palabra(pal)
            sys.exit(0)


def preguntar_palabra(pal):
    pal = ["", ""]
    for i in range(2):
        if i == 0:
            print("Ingresa una palabra o letra")
            pal[i] = inputs(var)
        elif i == 1:
            print("Ingrese la misma palabra, pero en mayuscula")
            pal[i] = inputs(var)
        try:
            if pal[i] == "":
                print("No se puede introducir nada")
                return ["Error", ""]
            pal[i] = int(pal[i])
            print("No se puede introducir solo números")
            return ["Error", ""]
        except Exception:
            for x in range(10):
                x = str(x)
                letra = pal[i].find(x)
                try:
                    letra = int(letra)
                    if letra != -1:
                        print("No se puede introducir números a la",
                              "vez que letras")
                        return ["Error", ""]
                except Exception:
                    pass
    if pal[1].upper == pal[1]:
        return pal
    else:
        print("La palabra tiene que estar toda en mayusculas")
        return "Error"


def proceso_palabra(pal):
    letra = ["", ""]
    if pal[0] == pal[1].lower():
        print("Las palabras son iguales")
        return "Las palabras son iguales"
    else:
        print("Las palabras son diferentes")
        return "Las palabras son diferentes"
    # for i in range(len(pal[0])):
    #     letra[0, 1] = pal[0][i, i+1], pal[1][i, i+1]
    #     try:
    #         if letra[0] == letra[1]:
    #             pass
    #         else:
    #             return "No son iguales"
    #     except Exception:
    #         pass

if __name__ == "__main__":
    var = ""
    loop_preguntar_palabra("")
