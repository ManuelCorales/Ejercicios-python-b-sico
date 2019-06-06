# Los números tienen que ser de 10 cifras


def loop_preguntar_nombre():
    """Esta función es la encargada de ejecutar todas las demás
    No recibe ni devuelve ningun parametro, por lo tanto no es
    considerada testeable"""
    dic_nombre = {"carlos": "1165329856",
                  "ruben": "1123654875",
                  "jorge": "1156236235"}
    while True:
        nombre = preguntar_nombre("")
        if nombre == "Error":
            continue
        if proceso_nombre(nombre, dic_nombre) == "No se encontró el nombre":
            rta_crear_o_no_telefono = crear_o_no_telefono("")
            if rta_crear_o_no_telefono == "Crear teléfono":
                nuevo_telefono = crear_telefono(nombre, "")
                if nuevo_telefono == "Error":
                    print("Ingresó cualquier cosa, por lo tanto no se va",
                          "a crear el telefono de " + nombre)
                    continue
                elif nuevo_telefono == "Volver a preguntar nombre":
                    continue
                else:
                    dic_nombre[nombre] = nuevo_telefono
                    print("Teléfono creado correctamente")
        else:
            rta_si_o_no_editar_telefono = si_o_no_editar_telefono("")
            if rta_si_o_no_editar_telefono == "Editar teléfono":
                telefono_editado = editar_telefono(nombre, "")
                if telefono_editado == "Error":
                    print("Ingresó cualquier cosa, por lo tanto no se va",
                          "a editar el telefono de " + nombre)
                    continue
                elif telefono_editado == "Volver a preguntar nombre":
                    continue
                else:
                    dic_nombre[nombre] = telefono_editado
                    print("Teléfono editado correctamente")


def crear_telefono(nombre, nuevo_telefono):
    """Recibe el parametro nombre y junto con 'nuevo_telefono'
    """
    print("Introduzca el nuevo telefono que quiere asignarle a " + nombre)
    nuevo_telefono = inputs(nuevo_telefono)
    try:
        nuevo_telefono = int(nuevo_telefono)
        nuevo_telefono = str(nuevo_telefono)
        if len(nuevo_telefono) == 10:
            return nuevo_telefono
        else:
            return "Error"
    except Exception:
        print("Solo se pueden ingresar números")
        return "Error"


def editar_telefono(nombre, telefono_editado):
    """Recibe los dos parametros y con ellos hace un print.
    Además, devuelve el número de teléfono editado"""
    print("Introduzca el nuevo telefono que quiere asignarle a " + nombre)
    telefono_editado = inputs(telefono_editado)
    try:
        telefono_editado = int(telefono_editado)
        telefono_editado = str(telefono_editado)
        if len(telefono_editado) == 10:
            return telefono_editado
        else:
            return "Error"
    except Exception:
        print("Solo se pueden ingresar números")
        return "Error"


def si_o_no_editar_telefono(si_o_no):
    """Recibe 'si_o_no' unicamente para ser testeada
    y devuelve 'Volver a preguntar nombre' en caso de
    que no se quiera editar el número. Y en caso contrario
    devuelve 'Editar teléfono'"""
    print("Desea editar el teléfono? Escriba 'Si', o 'No'")
    si_o_no = ((inputs(si_o_no)).lower()).strip()
    if si_o_no == "no":
        return "Volver a preguntar nombre"
    elif si_o_no == "si":
        return "Editar teléfono"


def crear_o_no_telefono(si_o_no):
    print("Desea crear un teléfono para ese contacto? Ingrese 'Si' o 'No'")
    si_o_no = ((inputs(si_o_no)).lower()).strip()
    if si_o_no == "no":
        return "No crear"
    elif si_o_no == "si":
        return "Crear teléfono"


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


def preguntar_nombre(nombre):
    """Evalúa si la nombre ingresada no contiene números
    ni esta vacía. En cualquiera de los dos casos devuelve
    'Error'"""
    print("Teléfono de quién desea saber?")
    nombre = inputs(nombre)
    try:
        if nombre.strip() == "":
            print("No se puede introducir solo espacios o nada")
            return "Error"
        nombre = int(nombre)
        print("No se pueden introducir solo números")
        return "Error"
    except Exception:
        for i in range(10):
            i = str(i)
            letra = nombre.find(i)
            try:
                letra = int(letra)
                if letra != -1:
                    print("No se puede introducir números a la vez que letras")
                    return "Error"
            except Exception:
                pass
    return (nombre.strip()).lower()


def proceso_nombre(nombre, dic_nombre):
    """Recibe el nombre ingresado junto con el diccionario de nombres.
    Lo busca, y si lo encuentra devuelve: 'No se encontró el nombre'
    y devuelve el teléfono en caso contrario"""
    if nombre in dic_nombre:
        print("El telefono de " + nombre + " es: " + dic_nombre[nombre])
        return dic_nombre[nombre]
    else:
        print("No se encontró el nombre")
        return "No se encontró el nombre"
if __name__ == "__main__":
    loop_preguntar_nombre()
