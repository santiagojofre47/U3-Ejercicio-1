from claseManejador import manejadorFacultad
from claseMenu import Menu

if __name__ == '__main__':
    unMenu = Menu()
    unManejador = manejadorFacultad()
    unManejador.leerArchivo()
    unMenu.mostrarMenu(unManejador)