def suma(a,b):
    #archivo de FUNCIONES
    print ("la suma de ",a," y ",b," es-> ",a+b)

def resta(a,b):
    print ("la resta de ",a," y ",b," es-> ",a-b)

def multiplicacion(a,b):
    print ("la multiplicacion de ",a," y ",b," es-> ",a*b)

def division(a,b):
    print ("la division de ",a," y ",b," es-> ",a/b)

def mod(a,b):
    print ("la mod de ",a," y ",b," es-> ",a%b)

def suma_varios(num):
    temp = 0

    for i in range(len(num)):
        temp = temp + num[i];

    return temp
