puntos=[[0,0],[0,0],[0,0]]

tabla=[1,2,3]

dist=[0,0,0]

XoY="X"

for i in range (3):
    for z in range (2):
        print("Ingrese un valor en",XoY, "para el punto ",(i+1))
        puntos[i][z]=int(input())
        if XoY == "X" :
            XoY="Y"
        else:
            XoY="X"
raiz=1/2

for i in range (3):
    dist[i]=float(((puntos[i][0])**2 + (puntos[i][1])**2)**(1/2))

print(sorted(tabla, key = dist))
"""print("El punto que mas cerca esta del centro de coordenadas es el punto" )"""