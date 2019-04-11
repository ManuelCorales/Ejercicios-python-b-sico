import time
print ("Todas las posibles piesas de domino en...")
for i in range (3,0,-1):
    print (i,"...")
    time.sleep(1)

x=0

for i in range (7):
    for z in range (x,7):
        print (i,"- | -",z)
    x += 1