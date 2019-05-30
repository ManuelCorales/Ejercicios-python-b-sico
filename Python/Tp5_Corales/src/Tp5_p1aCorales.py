"""La contraseña es '123'"""
"""La cantidad máxima de veces que se puede probar una contraseña son 5"""


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
            continue


def preguntar_contrasena(var):
    print("Introduzca una contraseña-")
    contrasena = ""
    contrasena = inputs(var)
    if contrasena == "123":
        print("Contraseña correcta")
        return contrasena
    else:
        print("Contraseña incorrecta")
        return contrasena
if __name__ == "__main__":
    loop_preguntar_contrasena()
