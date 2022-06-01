class Carrera:
    __Codigo = None
    __Nombre = None
    __Duracion = None
    __Titulo = None

    def __init__(self, codigo = None, nombre = None, duracion = None, titulo = None):
        self.__Codigo = codigo
        self.__Nombre = nombre
        self.__Duracion = duracion
        self.__Titulo = titulo

    def getNombre(self):
        return self.__Nombre

    def getDuracion(self):
        return self.__Duracion

    def getCodigo(self):
        return self.__Codigo    


    '''def __str__(self):
        return 'Codigo: {} Nombre: {} Duracion: {} Titulo: {}' .format(self.__Codigo, self.__Nombre, self.__Duracion, self.__Titulo)'''        