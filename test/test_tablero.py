import unittest
from tablero import Tablero, PosOcupadaException, PosicionInvalidaException

class TestTablero(unittest.TestCase):
    def test_poner_ficha_y_leer(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        self.assertEqual(t.contenedor[0][0], "X")

    def test_posicion_invalida(self):
        t = Tablero()
        with self.assertRaises(PosicionInvalidaException):
            t.poner_la_ficha(3, 0, "X")
        with self.assertRaises(PosicionInvalidaException):
            t.poner_la_ficha(0, 3, "X")

    def test_pos_ocupada(self):
        t = Tablero()
        t.poner_la_ficha(1, 1, "O")
        with self.assertRaises(PosOcupadaException):
            t.poner_la_ficha(1, 1, "X")

    def test_tres_en_linea_fila(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        t.poner_la_ficha(0, 1, "X")
        t.poner_la_ficha(0, 2, "X")
        self.assertTrue(t.hay_tres_en_linea("X"))

    def test_tres_en_linea_columna(self):
        t = Tablero()
        t.poner_la_ficha(0, 2, "O")
        t.poner_la_ficha(1, 2, "O")
        t.poner_la_ficha(2, 2, "O")
        self.assertTrue(t.hay_tres_en_linea("O"))

    def test_tres_en_linea_diagonal(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        t.poner_la_ficha(1, 1, "X")
        t.poner_la_ficha(2, 2, "X")
        self.assertTrue(t.hay_tres_en_linea("X"))

    def test_lleno(self):
        t = Tablero()
        fichas = ["X", "O"]
        k = 0
        for f in range(3):
            for c in range(3):
                t.poner_la_ficha(f, c, fichas[k % 2])
                k += 1
        self.assertTrue(t.lleno())

    
    def test_inicio_sin_tres_en_linea(self):
        t = Tablero()
        self.assertFalse(t.hay_tres_en_linea("X"))
        self.assertFalse(t.hay_tres_en_linea("O"))

    def test_str_muestra_guiones(self):
        t = Tablero()
        texto = str(t)
        self.assertIn("-", texto)  

    def test_fuera_de_rango_negativo(self):
        t = Tablero()
        with self.assertRaises(PosicionInvalidaException):
            t.poner_la_ficha(-1, 0, "X")
        with self.assertRaises(PosicionInvalidaException):
            t.poner_la_ficha(0, -1, "X")

if __name__ == "__main__":
    unittest.main()
