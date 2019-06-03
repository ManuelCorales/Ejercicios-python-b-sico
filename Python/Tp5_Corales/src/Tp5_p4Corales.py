# Las unicas cadenas que se admiten son las que no tienen numeros.

# La primera palabra ingresada siempre debe estar en minusculas en su
# totalidad, así como la segunda debe estar completamente en mayusculas
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


def loop_preguntar_palabra(pal):
    """Itera la función preguntar_palabra hasta
    que las dos palabras introducidas sean validas.
    Luego ejecuta proceso_palabra"""
    pal = ["", ""]
    while True:
        pal = preguntar_palabra(pal)
        if pal[0] == "Error":
            continue
        else:
            proceso_palabra(pal)
            sys.exit(0)


def preguntar_palabra(pal):
    for i in range(2):
        if i == 0:
            print("Ingresa una palabra o letra")
            pal[i] = inputs(pal[i])
        elif i == 1:
            print("Ingrese la misma palabra, pero en mayuscula")
            pal[i] = inputs(pal[i])
        try:
            if pal[i].strip() == "":
                print("No se puede introducir solo espacios o nada")
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
        if i == 0:
            if pal[0].lower() == pal[0]:
                pass
            else:
                print("La palabra tiene que estar toda en minusculas")
                return ["Error", ""]
    if pal[1].upper() == pal[1]:
        return pal
    else:
        print("La palabra tiene que estar toda en mayusculas")
        return ["Error", ""]


def proceso_palabra(pal):
    if pal[0] == pal[1].lower():
        print("Las palabras son iguales")
        return "Las palabras son iguales"
    else:
        print("Las palabras son diferentes")
        return "Las palabras son diferentes"

if __name__ == "__main__":
    var = ""
    loop_preguntar_palabra("")
