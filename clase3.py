def main():
    edad = int(input("que edad tiene: "))

    #IF - ELSE
    if(edad > 18):
        print("mayor de edad")
    else:
        print("menor de edad")

    if(edad > 18):
        if(edad < 60):
            print("puede hacer servicio militar")
        else:
            print("es demasiado viejo para el servicio militar")
    else:
        print("es demasiado joven para el servicio militar")

    #ELIF
    pais = input("de que pais eres: ")
    if(pais =="mex"):
        print("es mexicano")
    elif(pais =="per"):
        print("es peruano")
    elif(pais == "arg"):
        print("eres argentino")
    else:
        print("eres de un pais desconocido")
main()
