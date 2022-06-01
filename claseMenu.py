from claseManejador import manejadorFacultad

class Menu:
    __opcion = 0

    def mostrarMenu(self,unManejador):
        if isinstance(unManejador, manejadorFacultad):
            salir = False
            while not salir:
                print('\n')
                print('a- Mostrar carreras de una facultad dada')
                print('b- Mostrar datos de la facultad en donde se dicta una carrera dada')
                print('c - Salir')
                self.__opcion = input('Ingrese una opcion: ')

                if self.__opcion.lower() == 'a':
                    self.EjecutarA(unManejador)
                elif self.__opcion.lower() == 'b':
                    self.ejecutarB(unManejador)
                elif self.__opcion.lower() == 'c':
                    salir = True
                    del unManejador
                    print('Cerrando menu...')
                else:
                    print('ERROR: opcion ingresada incorrecta!')
                    input('Presione ENTER para continuar')        

    def EjecutarA(self, unManejador):
        entero = False
        while not entero:
            try:
                codigo = int(input('Ingrese el codigo de una facultad: '))
                unManejador.mostrarDatosFacultad(codigo)
            except ValueError:
                print('Error el valor ingresado no es un entero!')
            else:
                entero = True

    def ejecutarB(self,unManejador):
        nombre = input('Ingrese el nombre de una carrera: ')
        unManejador.mostrarDatosCarrera(nombre)