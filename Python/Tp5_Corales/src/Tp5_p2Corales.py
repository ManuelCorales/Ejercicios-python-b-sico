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
    print("Ingresa una palabra o letra")
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
    """Evalua cuántas letras 'A' y 'E' tiene la palabra ingresada
    En caso de tener más 'E' devuelve 'Hay más letras E'.
    En caso de tener más 'A' devuelve 'Hay más letras A'
    En caso de que no haya ninguna de las dos letras devuelve
    'No contiene ninguna de las dos letras'"""
    largo = len(pal)
    a = 0
    e = 0
    for i in range(len(pal)):
        letra = pal[i: i+1]
        try:
            if letra.lower() == "a":
                a += 1
            elif letra.lower() == "e":
                e += 1
        except Exception:
            pass
    cantidadAE = [a, e]
    cantidadAE[0] = str(cantidadAE[0])
    cantidadAE[1] = str(cantidadAE[1])
    if cantidadAE[0] == "0" and cantidadAE[1] == "0":
        print("La cadena ingresada no tiene letras 'a' ni 'e'")
        return "No contiene ninguna de las dos letras"
    else:
        print("La cadena tiene " + cantidadAE[0] + " letras 'A' y " +
              cantidadAE[1] + " letras 'E'")
        if cantidadAE[0] > cantidadAE[1]:
            print("Por lo tanto, hay más letras A")
            return "Hay más letras A"
        else:
            print("Por lo tanto, hay más letras E")
            return "Hay más letras E"


if __name__ == "__main__":
    loop_preguntar_palabra("")
