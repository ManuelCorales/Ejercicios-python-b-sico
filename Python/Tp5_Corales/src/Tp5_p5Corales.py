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
    """Evalúa si la palabra ingresada no contiene números
    ni esta vacía. En cualquiera de los dos casos devuelve
    'Error'"""
    print("Ingresa una cadena de palabras")
    pal = inputs(pal)
    try:
        if pal == "":
            print("No se pueden introducir nada")
            return "Error"
        pal = int(pal)
        print("No se pueden introducir solo números")
        return "Error"
    except Exception:
        for i in range(10):
            i = str(i)
            letra = pal.find(i)
            try:
                letra = int(letra)
                if letra != -1:
                    print("No se puede introducir números a la vez que letras")
                    return "Error"
            except Exception:
                pass
    return pal


def proceso_palabra(pal):
    primerletra = pal[0: 1].upper()
    for i in range(len(pal)):
        caracter = pal[i: i+1]
        if caracter == " ":
            primerletra += pal[i+1: i+2].upper()
    print(primerletra)
    return(primerletra)
if __name__ == "__main__":
    loop_preguntar_palabra("")
