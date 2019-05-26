import sys


def inputs(var):
    """Se encarga de hacer un input cada vez que se la llama"""
    if __name__ == "__main__":
        val = input()
        return val
    else:
        return var


def loop_ingreso_datos(cant_ejer, cant_nece):
    """Se encarga de loopear las funciones ingreso_dato_cant_ejer
    e ingreso_dato_cant_nece hasta que se introduzcan los valores
    que deberian ser ingresados"""
    while True:
        cant_ejer = ingreso_dato_cant_ejer(cant_ejer)
        if cant_ejer == "Error cant_ejer":
            continue
        while True:
            cant_nece = ingreso_dato_cant_nece(cant_ejer, cant_nece)
            if cant_nece == "Error cant_nece":
                continue


def ingreso_dato_cant_ejer(cant_ejer):
    """Pregunta cuantos ejercicios tiene el examen"""
    print("Cuantos ejercicios tiene cada examen?")
    cant_ejer = inputs(cant_ejer)
    try:
        cant_ejer = int(cant_ejer)
        if 2 > cant_ejer or cant_ejer > 100:
            print("El mínimo de ejercicios por examen son 2 y máximo 100")
            return "Error cant_ejer"
        else:
            return cant_ejer
    except Exception:
        print("No se puede introducir cualquier cosa diferente de números")
        return "Error cant_ejer"


def ingreso_dato_cant_nece(cant_ejer, cant_nece):
    """Pregunta cual es el porcentaje de examen tiene que estar bien
    para que el alumno apruebe"""
    print("Cual es el porcentaje de ejercicios que deben estar",
          "correctos para que el alumno apruebe? ")
    cant_nece = inputs(cant_nece)
    try:
        cant_nece = int(cant_nece)
        if 0 > cant_nece or cant_nece > 100:
            print("No puede ser más del 100% o menor a 0 ")
            return "Error cant_nece"
        else:
            if __name__ == "__main__":
                loop_proceso_notas(cant_ejer, cant_nece, 0)
            return cant_nece
    except Exception:
        print("No se puede introducir cualquier cosa diferente de números")
        return "Error cant_nece"


def loop_proceso_notas(cant_ejer, cant_nece, cant_corr):
    """Itera la funcion proceso_notas hasta que el usuario meta el
    caracter "*" """
    i = 1
    while True:
        comodin = proceso_notas(cant_ejer, cant_nece, cant_corr, i)
        # comodín almacena la devolucuion de la función proceso notas
        if comodin == "Error":
            continue
        elif comodin == "*":
            sys.exit(0)
        else:
            i += 1


def proceso_notas(cant_ejer, cant_nece, cant_corr, i):
    """Determina qué alumnos aprobaron segun cuantos ejercicios tenía la
    prueba, el porcentaje de examen que tiene que estar bien
    para que el alumno apruebe y la cantidad de ejercicios
    hechos correctamente"""
    print("Cuantos ejercicios resolvio correctamente el alumno ", i, "?")
    cant_corr = inputs(cant_corr)
    try:
        if cant_corr == "*":
            print("Fin de la lista de alumnos")
            return "*"
        cant_corr = int(cant_corr)
        if cant_ejer < int(cant_corr):
            print("No pudo haber hecho más ejercicios de los que había")
            return "Error"
        elif 0 > cant_corr:
            print("No se pueden meter valores negativos")
            return "Error"
        else:
            if int(cant_corr) / cant_ejer >= cant_nece / 100:
                print("El alumno 1 resolvió el",
                      100 * (round(int(cant_corr) / cant_ejer, 2)),
                      "%", " del examen correctamente, por lo tanto aprobó")
                return "Aprobó"
            else:
                print("El alumno 1 resolvió el",
                      100*(round(int(cant_corr) / cant_ejer, 2)),
                      "%", "del examen correctamente, por lo tanto, desaprobó")
                return "Desaprobó"
    except Exception:
        print("No se puede ingresar cualquier cosa diferente de números")
        return "Error"

if __name__ == "__main__":
    loop_ingreso_datos(0, 0)
