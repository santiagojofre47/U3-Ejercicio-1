import csv
from claseFacultad import Facultad
from claseCarrera import Carrera


class manejadorFacultad:
    __listaFacultad = None

    def __init__(self):
        self.__listaFacultad = []

    def agregarFacultad(self, unaFacultad):
        if isinstance(unaFacultad, Facultad):
            self.__listaFacultad.append(unaFacultad)

    def leerArchivo(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo, delimiter = ',')
        bandera = False
        for fila in reader:
            if not fila[1].isdigit():
                unaFacultad = Facultad(int(fila[0]),fila[1],fila[2],fila[3],fila[4])
                bandera = True
                
            else:  
                UnaCarrera = Carrera(int(fila[1]),fila[2],fila[3],fila[4])
                unaFacultad.agregarCarrera(UnaCarrera)
                
            if bandera == True:
                self.agregarFacultad(unaFacultad) 
                bandera =False
        archivo.close()

    def mostrarDatosFacultad(self, codigo):
        if isinstance(codigo, int):
            encontro = False
            i = 0
            while i < len(self.__listaFacultad) and not encontro:
                if self.__listaFacultad[i].getCodigo() == codigo:
                    encontro = True
                    print('Nombre de la facultad: {}'.format(self.__listaFacultad[i].getNombre()))
                    print('Carreras que presenta:')
                    self.__listaFacultad[i].mostrarCarreras()
                else:
                    i+=1
            if not encontro:
                print('ERROR: facultad no encontrada!')        

    def mostrarDatosCarrera(self, nombre):
        i = 0
        encontro = False
        carrera = None
        while i < len(self.__listaFacultad) and not encontro:
            carrera = self.__listaFacultad[i].buscarCarrera(nombre)
            if  type(carrera) != Carrera:
                i+=1
            else:
                encontro = True
                print('Datos de la facultad: ')
                print('Codigo: {},{} Nombre: {} localidad: {}' .format(self.__listaFacultad[i].getCodigo(), carrera.getCodigo() , self.__listaFacultad[i].getNombre(), self.__listaFacultad[i].getLocalidad()))

        if not encontro:
            print('ERROR: carrera no encontrada!')

    def __del__(self):
        print('Liberando memoria...')
        i = 0
        while i < len(self.__listaFacultad):
            del self.__listaFacultad[i]



    ''' def __str__(self):
        i = 0
        s = ''
        while i < len(self.__listaFacultad):
            s+=str(self.__listaFacultad[i])+'\n'
            i+=1
        return s    '''