def dec_a_rom(num):
    """Lo que hace la función es pedir un valor y la transforma en romano y
    devuelve la variable num para ser procesada en la siguiente función"""
    print("Ingrese el número que quiera convertir al sistema romano")
    if __name__ == "__main__":
        num = input()
    return num


def loop_transformador_dec_a_rom(num):
    """Itera la función transformador_dec_a_rom hasta que
    se introduzca un numero valido"""
    while True:
        respuesta = transformador_dec_a_rom(dec_a_rom(0))
        if respuesta == "Error":
            continue
        else:
            return


def transformador_dec_a_rom(num):
    """Lo que hace es tomar la variable num de la función anterior y la usa
    para transformala en romanos"""
    decs = (1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000,
            10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50,
            40, 10, 9, 5, 4, 1)
    roms = ("m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv",
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V",
            "IV", "I")
    numfinal = ""
    try:
        num = int(num)
        if num > 1000000 or 0 > num:
            print("Solo permite números menores a 1.000.000 y mayores a 0")
            return "Error"
        for i in range(25):
            # 25 es la cantidad de combinaciones de caracteres romanos
            aux = int(num/decs[i])
            numfinal = numfinal + (roms[i] * aux)
            num -= (decs[i]*aux)
        print(numfinal, ". Los numeros en minuscula representan",
              "a su valor decimal multiplicado por 1000")
        return numfinal
    except Exception:
        print("No se pueden introducir caracteres que no sean números")
        return "Error"
if __name__ == "__main__":
    loop_transformador_dec_a_rom(0)
