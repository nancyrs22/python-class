def main():
    #declarar una cadena

    cadena = "hola mundo ke ace :v"

    print(cadena)
    print("tamaño de la cadena: ",len(cadena)) #len para obtener la cantidad de caracteres
    print()

    #acceder a un caracter y obtener una porcion de cadena
    print(cadena[0])
    print(cadena[0:5])
    print()

    #concatenacion
    s1 = "holi "
    s2 = "soy la zuky"
    s3 = s1 + s2
    print(s3)
    print()

    #comparar alfabeticamente
    s1 = "hola como esta"
    s2 = "hola como esta"
    if(s1 == s2):
        print("son iguales")
    else:
        print("son diferentes")
    print()

    #busqueda de cadenas
    if "hola" in s1:
        print("si esta")
    else:
        print("no esta")

    pos = s1.find("hola")
    print(pos)

    print()

    #reemplazo de texto
    print(s1)
    s1 = s1.replace("hola","holi")
    print(s1)

    #division y union de cadenas
    fecha = "25/02/2018"
    datos = fecha.split("/")
    print(datos[0])

    print("-".join(datos))

main()
