"""La contraseña es '123'"""


def inputs(var):
    """Se encarga de ejecutar un input cada vez que se la llama
    siendo ejecutada desde el mismo archivo. En caso de que el
    programa sea ejecutado por otro archivo, devuelve la mismva
    variable que se le ingresa"""
    if __name__ == "__main__":
        var = input()
        var = str(var)
        return var
    else:
        return var


def loop_preguntar_contrasena():
    """Itera la funcion preguntar_contrasena hasta que la
    contrasena introducida sea la correcta"""
    while True:
        respuesta = preguntar_contrasena("xd")
        if respuesta == "123":
            return "Contrasena correcta"
        else:
            continue


def preguntar_contrasena(var):
    print("Introduzca una contrasena-")
    contrasena = ""
    contrasena = inputs(var)
    if contrasena == "123":
        print("Contrasena correcta")
        return contrasena
    else:
        print("Contrasena incorrecta")
        return contrasena
if __name__ == "__main__":
    loop_preguntar_contrasena()