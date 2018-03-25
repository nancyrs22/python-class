import math
def main():

    #para seno, coseno,tangente
    ang = 45
    rad = ang*math.pi/180

    print("El seno de ",ang,"es-> ",math.sin(rad))
    print("El coseno de ",ang,"es-> ",math.cos(rad))
    print("El tangente de ",ang,"es-> ",math.tan(rad))

    print()

    #para raiz cuadrada y potencia
    print("Raiz cuadrada de 81 -> ",math.sqrt(81))
    print("9 al cuadrado->", math.pow(9,2))

    #valor absoluto, redondeo hacia arriba y abajo
    print("el valor absoluto de -35 ->",math.fabs(-35))
    print("redondeo hacia abajo de 3.55-> ",math.floor(3.55))
    print("redonde hacia arriba de 3.55->",math.ceil(3.55))

    #logaritmo en base 10 y exponencial
    print("logaritmo natural de 12-> ", math.log(12))
    print("logaritmo en base 10 de 12-> ", math.log10(12))
    print("e elevado al cubo-> ",math.exp(3))
main()
