class Zoologico:
    
    def __init__(self, nombre, ubicacion ):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
        
    
    def agregarZonas(zona):
        Zoologico._zonas.append(zona)

    def cantidadTotalAnimales():
        cont = 0
        for zona in Zoologico._zonas:
            cont += len(zona.getAnimales())
        return cont
                
    # setters and getters for nombre, ubicacion and zonas
    def setNombre (self, nombre):
        self._nombre = nombre
    
    def getNombre (self):
        return self._nombre
    
    def setUbicacion (self, ubicacion):
        self._ubicacion = ubicacion
    
    def getUbicacion (self):
        return self._ubicacion

    def setZona (self, zonas):
        self._zonas = zonas
    
    def getZona (self):
        return self._zonas

    

# Para la clase Zoológico el método cantidadTotalAnimales, retornara la cantidad de
# animales total de todas las zonas que tengan relación con el Zoológico,
# agregarZonas será el método encargado de agregar nuevas zonas al zoologico.

    
    