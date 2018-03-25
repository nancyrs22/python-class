print ("bienvenido al traductor")

palabra = input("que palabra deseas traducir: ")
#the method .isalpha() which returns False since the string contains non-letter characters.
if len(palabra) > 0 and palabra.isalpha():
    {
        print (palabra)
    }
else:
    print ("empty")
