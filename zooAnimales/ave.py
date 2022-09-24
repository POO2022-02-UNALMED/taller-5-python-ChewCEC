from zooAnimales.animal import Animal

class Ave (Animal):

    _listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
    
    def cantidadAves():
        return len(Ave._listado)

    def movimiento():
        pass

    @classmethod
    def crearHalcon(cls, nombre, edad, genero ):
        cls.halcones += 1
        halcon = Ave(nombre, edad, "montañas", genero, "cafe glorioso")
        return halcon

    @classmethod
    def crearAguila(cls, nombre, edad, genero ):
        cls.aguilas += 1
        aguila = Ave(nombre, edad, "montañas", genero, "blanco y amarillo")
        return aguila

    # setters and getters for colorPlumas and listado
    def setColorPlumas (self, colorPlumas):
        self._colorPlumas = colorPlumas
    
    def getColorPlumas (self):
        return self._colorPlumas
    
    def setListado (self, listado):
        self._listado = listado
    
    def getListado (self):
        return self._listado

# La clase Ave tendrá algunos comportamientos particulares, en el
# atributo halcones y aguilas se quiere llevar el conteo de veces
# que se usó el método crearHalcon y el método crearAguila y el
# metodo cantidadAves retornara la cantidad de aves creadas
# en el sistema.

#  Para la clase Ave el método crearHalcon, creará un Ave con los
# valores para colorPlumas = “cafe glorioso” y hábitat =
# “montanas”, los demás valores los recibirá como parámetros.

#  Para la clase Ave el método crearAguila, creará un Ave con
# los valores para colorPlumas = “blanco y amarillo” y hábitat
# = “montanas”, los demás valores los recibirá como
# parámetros.


