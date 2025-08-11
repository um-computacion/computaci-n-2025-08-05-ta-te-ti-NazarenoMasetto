class PosOcupadaException(Exception):
    pass

class PosicionInvalidaException(Exception):
    pass

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def esta_en_rango(self, fila, columna):
        if fila >= 0 and fila < 3 and columna >= 0 and columna < 3:
            return True
        else:
            return False

    def celda_vacia(self, fila, columna):
        if self.contenedor[fila][columna] == "":
            return True
        else:
            return False

    def poner_la_ficha(self, fila, columna, ficha):
        if not self.esta_en_rango(fila, columna):
            raise PosicionInvalidaException("Posicion fuera del tablero (0-2).")
        if not self.celda_vacia(fila, columna):
            raise PosOcupadaException("Esa casilla ya tiene algo.")
        self.contenedor[fila][columna] = ficha

    def hay_tres_en_linea(self, ficha):
        # para filas
        for f in range(3):
            if self.contenedor[f][0] == ficha and self.contenedor[f][1] == ficha and self.contenedor[f][2] == ficha:
                return True
        # para columnas
        for c in range(3):
            if self.contenedor[0][c] == ficha and self.contenedor[1][c] == ficha and self.contenedor[2][c] == ficha:
                return True
        # para diagonales
        if self.contenedor[0][0] == ficha and self.contenedor[1][1] == ficha and self.contenedor[2][2] == ficha:
            return True
        if self.contenedor[0][2] == ficha and self.contenedor[1][1] == ficha and self.contenedor[2][0] == ficha:
            return True
        return False

    def lleno(self):
        for f in range(3):
            for c in range(3):
                if self.contenedor[f][c] == "":
                    return False
        return True

    def __str__(self):
        filas = []
        for f in range(3):
            fila_texto = ""
            for c in range(3):
                if self.contenedor[f][c] == "":
                    fila_texto += "-"
                else:
                    fila_texto += self.contenedor[f][c]
                if c < 2:
                    fila_texto += " | "
            filas.append(fila_texto)
        return "\n".join(filas)
