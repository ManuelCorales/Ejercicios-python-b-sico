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
        if pal.strip() == "":
            print("No se puede introducir solo espacios o nada")
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
    return pal.strip()


def proceso_palabra(pal):
    """Recibe el parametro 'pal' y cambia cada una de las letras que estan en
    las palabras que no comienzan con la letra 'a' tanto en minuscula como
    mayuscula. Devuelve una cadena solo con las palabras que empiezan con 'a'
    """
    # Cuando rango_palabra se iguala a True indica que se encontró una palabra
    # que empieza con una letra diferente a la "a" evaluando si el caracter es
    # un espacio y si su siguiente es una letra que no cumple con la regla.
    # Después de eso cuando se reconoce un nuevo espacio, se fija rango_palabra
    # a False, indicando que termino la palabra
    #
    pal = list(pal)
    rango_palabra = False
    if pal[0].lower() != "a":
        rango_palabra = True
    for i in range(len(pal)):
        if pal[i] == " " and pal[i+1].lower() != "a":
            rango_palabra = True
        else:
            if pal[i] == " ":
                rango_palabra = False
        if rango_palabra is True:
            pal[i] = ""
    pal = ("".join(pal)).strip()
    print("La cadena quedaría: " + pal)
    return pal
if __name__ == "__main__":
    loop_preguntar_palabra("")
