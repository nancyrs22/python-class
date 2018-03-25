def main():
    #ARRAYS
    v = [1,2,3,4,5,6,7,8,9,0]

    for i in v:
        print(i," ",end="")
    print() #este print solo es para darle un espacio

    v.append(99) #para agregar elementos al array,agrega al final

    for i in range(len(v)): #otra manera de recorrer el arreglo, el metodo len devuelve el numero de elementos del array
        print(v[i]," ",end="")
    print()

    v.insert(1,54) #otro modo de agregar elemtos al array parecido al apprend, agrega al inicio

    for i in range(len(v)):
        print(v[i], " ", end = "")
    print()

    #para eliminar un elemento del arreglo
    del v[0]
    #del v[0]
    #del v[0]
    for i in range(len(v)):
        print(v[i], " ", end = "")

    print("\n")

    #MATRICES
    m = [[1,2,3],[4,5,6],[7,8,9]]

    m[0][0] = 3
    m[0][1] = 1
    m[0][2] = 2

    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], " ", end = "")
        print()
main()
