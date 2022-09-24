
class Animal():

    _totalAnimales = 0
    def __init__ (self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad =  edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        __totalAnimales += 1
    
    def cantidadTotalAnimales():
        return Animal.__totalAnimales

    def movimiento ():
        pass

    @classmethod
    def totalPorTipo (cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.reptil import Reptil
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        return f"Mamiferos: {Mamifero.cantidadMemiferos()} \nAves: {Ave.cantidadAves()} \nReptiles: {Reptil.cantidadReptiles()} \nPeces: {Pez.cantidadPeces()} \nAnfibios: {Anfibio.cantidadAnfibios()}"

    def toString(self):
        if self._zona == None:
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero()
        else:
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero() + ", la zona en la que me ubico es " + self._zona[0].getNombre() + ", en el " + self._zona[0].getZoo().getNombre()

# Para la clase Animal tenemos ciertas particularidades, queremos llevar el conteo del
# total de animales creados y que este valor podamos almacenarlo en el atributo
# totalAnimales, el método totalPorTipo, devolverá el siguiente formato con la
# cantidad de animales por cada subclase de animales:
# “Mamiferos: #
# Aves: #
# Reptiles: #
# Peces: #
# Anfibios: #“
# # es el numero de animales por cada subclase


    def setNombre (self, nombre):
        self._nombre = nombre

    def getNombre (self):
        return self._nombre

    def setEdad (self, edad):
        self._edad = edad

    def getEdad (self):
        return self._edad

    #Create setter and getter for habitat, genero and zona
    def setHabitat (self, habitat):
        self._habitat = habitat
    
    def getHabitat (self):
        return self._habitat

    def setGenero (self, genero):
        self._genero = genero

    def getGenero (self):
        return self._genero

    def setZona (self, zona):
        self._zona = zona
    
    def getZona (self):
        return self._zona
    
