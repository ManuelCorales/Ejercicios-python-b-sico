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
    """Itera la funcion preguntar_palabra hasta que la
    palabra introducida sea la valida. Luego ejecuta la función
    proceso_palabra y por ultimo sale del programa entero"""
    while True:
        pal = preguntar_palabra(pal)
        if pal == "Error":
            continue
        else:
            proceso_palabra(pal)
            sys.exit(0)


def preguntar_palabra(pal):
    """Evalúa si la palabra ingresada son números
    ni esta vacía. En cualquiera de los dos casos devuelve
    'Error'"""
    print("Ingresa una palabra o letra")
    pal = inputs(pal)
    if pal.strip() == "":
        print("No se pueden introducir solo espacios o nada")
        return "Error"
    try:
        pal = int(pal)
        print("No se pueden introducir solo números")
        return "Error"
    except Exception:
        return pal


def proceso_palabra(pal):
    """Se encarga de evaluar cuántas vocales tiene la palabra.
    Devuelve la cantidad de vocales"""
    largo = len(pal)
    vocales = 0
    for i in range(largo):
        letra = pal[i: i+1]
        try:
            letra = letra.lower()
            if letra == "a":
                vocales += 1
            elif letra == "e":
                vocales += 1
            elif letra == "i":
                vocales += 1
            elif letra == "o":
                vocales += 1
            elif letra == "u":
                vocales += 1
        except Exception:
            pass
    vocales = str(vocales)
    print("La palabra tiene " + vocales + " vocales")
    return vocales

if __name__ == "__main__":
    loop_preguntar_palabra("")
