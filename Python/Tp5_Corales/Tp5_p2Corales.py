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
            proceso_palabra(pal)


def preguntar_palabra(pal):
    print("Ingresa una palabra o letra")
    pal = inputs(var)
    if pal == "":
        print("No se pueden introducir nada")
        return "Error"
    elif isinstance(pal, int):
        print("No se pueden introducir solo números")
        return "Error"


def proceso_palabra(pal):
    largo = len(pal)
    for i in range(len(pal)):
        letra = pal[i, i+1]
        try:
            if lower(letra) == "a":
                a += 1
            elif lower(letra) == "e":
                e += 1
        except Exception:
            pass
    return (a, e)
    print(e)
    print(a)
if __name__ == "__main__":
    var = ""
    loop_preguntar_palabra("")