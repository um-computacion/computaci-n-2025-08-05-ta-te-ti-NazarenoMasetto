from tablero import Tablero, PosOcupadaException, PosicionInvalidaException

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.juego_terminado = False
        self.ganador = None

    def cambiar_turno(self):
        if self.turno == "X":
            self.turno = "O"
        else:
            self.turno = "X"

    def ocupar_una_de_las_casillas(self, fila, columna):
        if self.juego_terminado:
            raise Exception("El juego ya termino.")

        self.tablero.poner_la_ficha(fila, columna, self.turno)

        if self.tablero.hay_tres_en_linea(self.turno):
            self.juego_terminado = True
            self.ganador = self.turno
            return

        if self.tablero.lleno():
            self.juego_terminado = True
            self.ganador = None
            return

        self.cambiar_turno()
