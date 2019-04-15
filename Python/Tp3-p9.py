cant_ejer = 0
cant_nece = 0
def input_nota ():
    cant_ejer = 0
    cant_nece = 0
    print("")
    cant_ejer = int(input("¿Cuantos ejercicios cada examen? "))
    cant_nece = int(input("Cual es el porcentaje de ejercicios que deben estar correctos para que el alumno apruebe? "))
    if cant_nece > 100:
        print ("No puede ser mas del 100 %")
        input_nota()
        return cant_ejer,cant_nece

def proceso_notas(cant_ejer,cant_nece):
    i = 0
    z = 2
    while z > 1:
        i += 1
        print("Cuantos ejercicios resolvio correctamente el alumno ", i)
        cant_corr = input()
        if cant_corr == "*":
            print ("Fin de la lista de alumnos")
            z = 0
            return
        if int(cant_corr) / cant_ejer > cant_nece / 100:
            print ("El alumno 1 resolvió el",round(int(cant_corr) / cant_ejer),"%"," del examen correctamente, por lo tanto aprobó")
        else:
            print("El alumno 1 resolvió el",round(int(cant_corr) / cant_ejer),"%"," del examen correctamente, por lo tanto, desaprobó")
        


input_nota()
proceso_notas(cant_ejer,cant_nece)