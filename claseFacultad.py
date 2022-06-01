from ast import Import
from claseCarrera import Carrera

class Facultad:
    __Codigo = None
    __Nombre = None
    __Direccion = None
    __Localidad = None
    __Telefono = None
    __ListaCarrera = None

 
    def agregarCarrera(self, unaCarrera):
        if isinstance(unaCarrera, Carrera):
            self.__ListaCarrera.append(unaCarrera)

    def __init__(self, codigo = None, Nombre = None, direccion = None, localidad = None, telefono = None):
        self.__Codigo = codigo
        self.__Nombre = Nombre
        self.__Direccion = direccion
        self.__Localidad = localidad
        self.__Telefono = telefono
        self.__ListaCarrera = []

    def getCodigo(self):
        return self.__Codigo

    def getNombre(self):
        return self.__Nombre

    def getLocalidad(self):
        return self.__Localidad    

    def mostrarCarreras(self):
        i = 0
        while i < len(self.__ListaCarrera):
            print('Carrera: {} duracion: {}'.format(self.__ListaCarrera[i].getNombre(),self.__ListaCarrera[i].getDuracion()))
            i+=1

    def buscarCarrera(self, nombre):
        i = 0
        encontro = False
        objeto = None
        while i < len(self.__ListaCarrera) and not encontro:                
            if self.__ListaCarrera[i].getNombre().lower() == nombre.lower():
                encontro = True
                objeto = self.__ListaCarrera[i]
            else:
                i+=1
        return objeto            

    def __del__(self):
        i = 0
        while i < len(self.__ListaCarrera):
            del self.__ListaCarrera[i]    

    '''def __str__(self):
        s = 'Codigo: {}, Nombre: {}, Direccion: {}, Localidad: {}, Telefono: {}\n'.format(self.__Codigo, self.__Nombre, self.__Direccion, self.__Localidad, self.__Telefono)
        for carrera in self.__ListaCarrera:
            s+= str(carrera)+'\n'
        return s'''
