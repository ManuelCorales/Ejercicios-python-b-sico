# La contraseña correcta es "123"
# La cantidad maxima que se pueden probar contraseñas son 5

import time


def inputs(var):
    """Se encarga de ejecutar un input cada vez que se la llama
    siendo ejecutada desde el mismo archivo. En caso de que el
    programa sea ejecutado por otro archivo, devuelve la misma
    variable que se le ingresa"""
    if __name__ == "__main__":
        var = input()
        var = str(var)
        return var
    else:
        return var


def loop_preguntar_contrasena():
    """Itera la funcion preguntar_contrasena hasta que la
    contraseña introducida sea la correcta"""
    segundos = 0
    i = 0
    while True:
        respuesta = preguntar_contrasena("")
        if respuesta == "123":
            return "Contraseña correcta"
        else:
            i += 1
            if i == 5:
                print("No es posible seguir probando contaseñas")
                return "No es posible seguir probando contaseñas"
            segundos = str(segundos + 5)
            print("Ahora debera esperar: " + segundos + " segundos")
            segundos = int(segundos)
            time.sleep(segundos)
            continue


def preguntar_contrasena(pal):
    """Procesa si la palabra introducida es correcta o no.
    Si lo es, devuelve True, si no lo es, develve False"""
    print("Introduzca una contraseña-")
    contrasena = ""
    contrasena = inputs(pal)
    if contrasena == "123":
        print("Contraseña correcta")
        return True
    else:
        print("Contraseña incorrecta")
        return False
if __name__ == "__main__":
    loop_preguntar_contrasena()
