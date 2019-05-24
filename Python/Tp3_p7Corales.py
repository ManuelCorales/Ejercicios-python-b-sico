
def input_datos():
    """Esta función sirve para ingresar los datos sobre el dia deseado"""
    # Devuelve el parametro "día" que se procesa en la funcion "que_dia_es"
    print("Ingrese el día del año")
    dia = int(input())
    return dia


def que_dia_es(dia):
    """Esta función compara datos de listas y muestra el día que es"""
    # Toma el parametro día, lo divide por 7 y segun el resto (que siempre
    # van a ser 7 restos posibles), indica que día de la semana es
    semana = ("Lunes", "Martes", "Miércoles", "Jueves",
              "Viernes", "Sábado", "Domingo")
    restos = (0.14, 0.29, 0.43, 0.57, 0.71, 0.86, 0)
    if isinstance(dia, (int)) is True and dia != "":
        for i in range(0, 7):
            if round((dia/7) - int(dia/7), 2) == restos[i]:
                diadesem = semana[i]
                return diadesem
    else:
        print("El caracter introducido es una letra, está mal")
        return False

if __name__ == "__main__":
    que_dia_es(input_datos())
