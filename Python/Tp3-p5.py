
n = int(input("Ingrese un valor: "))
empieza = True
linea=""

def armaje_De_Matriz_Identidad():
    """Esta funcion arma la tabla de identidad principalmente"""
    linea=""
    x=0
    armaje_De_Cuadro(True)
    for i in range (n):
        for z in range(n):
            if z==x:
                linea=linea+"1 "
            else:
                linea=linea+"0 "
        x +=1
        print ("║ ",linea,"║")
        linea=""
    empieza=False
    armaje_De_Cuadro(False)


def armaje_De_Cuadro(empieza):
    """Esta función arma el cuadro que envuelve a la matríz de identidad"""
    linea=""
    for p in range ((2*n)+5):
        if p==0:
            if empieza==True:
                linea = linea+"╔"
            else:
                linea = linea+"╚"
        elif p==((2*n)+4):
            if empieza==True:
                linea = linea+"╗"
            else:
                linea = linea+"╝"
        else:
            linea= linea+"═"
    print(linea)
    empieza=False
armaje_De_Matriz_Identidad()