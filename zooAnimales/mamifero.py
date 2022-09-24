from zooAnimales.animal import Animal

class Mamifero (Animal):
    caballos = 0
    leones = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self) 
        

    def cantidadMemiferos():
        return (Mamifero.caballos + Mamifero.leones)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballos+=1
        cls.__init__(cls, nombre , edad, "Pradera", genero, True, 4)
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        leones+=1
        cls.__init__(cls, nombre , edad, "Selva", genero, True, 4)
    
    # setters and getters for pelaje and patas
    def isPelaje (self, pelaje):
        self._pelaje = pelaje

    def getPelaje (self):
        return self._pelaje
    
    def setPatas (self, patas):
        self._patas = patas
    
    def getPatas (self):
        return self._patas


# La clase Mamifero tendrá algunos comportamientos particulares,
# en el atributo caballos y leones se quiere llevar el conteo de
# veces que se usó el método crearCaballo y el método crearLeon
# y el metodo cantidadMamiferos retornara la cantidad de
# mamíferos creados en el sistema.


#  Para la clase Mamifero el método crearCaballo, creará un
# Mamifero con los valores para pelaje = true, patas = 4 y hábitat
# = “pradera”, los demás valores los recibirá como parámetros.
# Para la clase Mamifero el método crearLeon, creará un
# Mamifero con los valores para pelaje = true, patas = 4 y hábitat
# = “selva”, los demás valores los recibirá como parámetros.


