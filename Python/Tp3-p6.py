import time
elec=""
xv=0
yv=0
def input_Usuario():
    """Esta función lo que hace es pedirle al usuario que operación quiere hacer"""
    print("")
    print("Qué desea hacer?:")
    print("")
    print("-Sacar el máximos o mínimo de una funcion cuadratica?-(Ingrese la letra ""a"")")
    print("")
    print("-Sacar las raices de una funcion cuadratica?-(Ingrese la letra ""b"")")
    print("")
    print("-O averiguar el punto de interseccion entre dos rectas?-(Ingrese la letra ""c"")")
    elec=str(input())
    if elec == "a" or elec == "b":
        input_aob()
    elif elec == "c":
        input_c()
    else:
        print("Caracter invalido")
        input_Usuario()

def input_aob():
    """Esta función lo que hace es llevar a cabo la opcion "a" o "b" dependiendo de lo que introduce el usuario en elec"""
    print("")
    coef_a=int(input("Ingrese el coeficiente a diferente de 0:"))
    
    if coef_a==0:
        print("No se puede ese numero")
        input_aob()
    print("")
    coef_b=int(input("Ahora el b:"))
    print("")
    coef_c=int(input("Y ahora el termino independiente:"))
    
    if elec == "a":
        xv =(-coef_b)/(2*coef_a)
        yv = (coef_a*((xv)**2))+(coef_b * xv)+coef_c

        if  coef_a > 0:
            print("Tiene un punto mínimo y se encuentra en:")
        else:
            print("Tiene un punto máximo y se encuentra en:")

        print("X =",xv)
        print("Y =",yv)
    else:
        xd=((coef_b**2)-(4*coef_a*coef_c))
        
        if ((coef_b**2)-(4*coef_a*coef_c)) > 0:
            x1 = (-(coef_b)+((coef_b**2)-(4*coef_a*coef_c))**(1/2))/(2*coef_a)
            x2 = (-(coef_b)-((coef_b**2)-(4*coef_a*coef_c))**(1/2))/(2*coef_a)
            print ("Las racíces de esta función estan en los puntos:")
            print ("X1 =", round(x1,3))
            print ("X2 =", round(x2,3))
        else:
            print("Esta función no tiene raíces reales")

def input_c():
    """Esta función lleva a cabo la opcion "c" """
    rectas = [[0,0],[0,0]]  #Estas dos parejas que se guardan en "rectas", el primer parametro de cada una, es la pendiente, y el segundo es el termino independiente

    for i in range (2):
          print("Ingrese una pendiente para la recta", i+1)
          rectas[i][0]=float(input())
          print("")
    
    if rectas[0][0] == rectas[1][0]:
        print("No puede ingresar dos rectas paralelas o potencialmente superpuestas")
        time.sleep(1)
        input_c()
    else:
        for i in range (2):
            print("Ingrese un termino independiente para la recta", i+1)
            rectas[i][1]=float(input())
            print("")
        xv = (rectas[1][1]-rectas[0][1])/(rectas[0][0]-rectas[1][0])
        yv = ((rectas[0][0]*xv) + rectas[0][1])
        print("Las rectas va a hacer contacto en las coordenadas:")
        print("X =",xv)
        print("Y =",yv)

input_Usuario()
