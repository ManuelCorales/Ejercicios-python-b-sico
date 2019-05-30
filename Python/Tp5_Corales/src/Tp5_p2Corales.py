def inputs(var):
    if __name__ == "__main__":
        var = input()
        return var
    else:
        return var


def loop_preguntar_palabra(pal):

    while True:
        pal = preguntar_palabra(pal)
        if pal == "Error":
            continue
        else:
            cantidadAE = proceso_palabra(pal)
            cantidadAE = int(cantidadAE[:])
            if cantidadAE[0] == "0" and cantidadAE[1] == "0":
                print("La cadena ingresada no tiene letras 'a' ni 'e'")
            else:
                print("La cadena tiene " + cantidadAE[0] + " letras 'A' y ",
                      + cantidadAE[1] + " letras 'E'")


def preguntar_palabra(pal):
    print("Ingresa una palabra o letra")
    var = ""
    pal = inputs(var)
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
    return [a, e]

if __name__ == "__main__":
    loop_preguntar_palabra("")
