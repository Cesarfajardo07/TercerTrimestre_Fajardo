'''
1.Crear una clase que permita instanciar un objeto de la clase pais (maximo 4 atributos): PRIMERO NOMBRE, OTROS TRES DATOS NUMERICOS
2.Apliacar 2 funciones con algun dato estdistico y el resultado se guarda en otro archivo como texto

'''

class pais:
    def __init__(self, nombre,poblacion,altura,pop_cap):
        self.__nombre=nombre
        self.__poblacion=poblacion
        self.__altura=altura
        self.__pop_cap=pop_cap

    def info(self):
        return f"{self.__nombre} {self.__poblacion} {self.__altura} {self.__pop_cap}"

    def getNombre(self):
        return self.__nombre

    def getPoblacion(self):
        return self.__poblacion

    def getAltura(self):
        return self.__altura

    def getPop_cap(self):
        return self.__pop_cap

















