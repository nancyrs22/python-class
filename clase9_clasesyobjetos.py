class perro:
    patas = 4
    nombre = ""

    def nombrar(self, n ): #es un metodo porque esta dentro de una clase
        self.nombre = n
mascota = perro()
mascota2 = perro()

mascota.nombrar("tom")
mascota2.nombrar("rex")
print("tengo un perro, se llama %s y tiene %s patas"%(mascota.nombre,mascota.patas))
print("tengo otro perro, se llama %s y tambien tiene %s patas"%(mascota2.nombre,mascota2.patas))
