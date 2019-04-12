def dec_a_rom ():
    """Lo que hace la función es pedir un valor y la transforma en romano"""
    decs = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
    roms = ("M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I")
    numfinal = ""
    num = int(input("Ingrese el número que quiera convertir al sistema romano"))
    if num > 3999 or 0 > num:
        print("Solo permite números menores a 3999 y mayores a 0")
        dec_a_rom()
        return
    for i in range (13):
        aux = int(num/decs[i])
        numfinal =  numfinal + (roms[i] * aux)  
        num -= (decs[i]*aux)

    print(numfinal)
dec_a_rom ()

