preg= True

def convFahrCel(fahr):
    """Esta funcion lo que hace es procesar el dato ingresado y procesarlo almacenarlo en la variable cel (Celcius) """
    
    cel= (fahr-32)*5/9
    
    if preg == True:
        """Este if sirve para mostrar solo 1 vez el comando print del dato ingresado por el usuario"""
        print ("Esos son {} °C".format (cel))
    
    return cel

fahr=int(input ("Ingrese una temperatura Fahrenheit que desea transformar a Celcius: "))

convFahrCel(fahr)

preg = False


def tabla (cel):
    """Esta funcion lo que hace es mostrar la tabla de equivalencias entre °F y °C"""
    
    while len str(i) != 3:
        str (i) = "" + str(i)

    print (str(i),"°F | ",str(cel)[:4],"°C" )

for i in range (0,201,10):
    tabla(convFahrCel(i))
