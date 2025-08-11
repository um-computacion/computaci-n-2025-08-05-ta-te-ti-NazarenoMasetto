import unittest
from tateti import Tateti

class TestTateti(unittest.TestCase):
    def test_cambia_turno_luego_de_jugar(self):
        juego = Tateti()
        self.assertEqual(juego.turno, "X")
        juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(juego.turno, "O")

    def test_gana_x_en_fila(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0)  # X
        juego.ocupar_una_de_las_casillas(1, 0)  # O
        juego.ocupar_una_de_las_casillas(0, 1)  # X
        juego.ocupar_una_de_las_casillas(1, 1)  # O
        juego.ocupar_una_de_las_casillas(0, 2)  # X gana
        self.assertTrue(juego.juego_terminado)
        self.assertEqual(juego.ganador, "X")

    def test_empate(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0)  # X
        juego.ocupar_una_de_las_casillas(0, 1)  # O
        juego.ocupar_una_de_las_casillas(0, 2)  # X
        juego.ocupar_una_de_las_casillas(1, 1)  # O
        juego.ocupar_una_de_las_casillas(1, 0)  # X
        juego.ocupar_una_de_las_casillas(1, 2)  # O
        juego.ocupar_una_de_las_casillas(2, 1)  # X
        juego.ocupar_una_de_las_casillas(2, 0)  # O
        juego.ocupar_una_de_las_casillas(2, 2)  # X
        self.assertTrue(juego.juego_terminado)
        self.assertIsNone(juego.ganador)

    def test_no_se_puede_jugar_si_termino(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0)
        juego.ocupar_una_de_las_casillas(1, 0)
        juego.ocupar_una_de_las_casillas(0, 1)
        juego.ocupar_una_de_las_casillas(1, 1)
        juego.ocupar_una_de_las_casillas(0, 2)
        self.assertTrue(juego.juego_terminado)
        with self.assertRaises(Exception):
            juego.ocupar_una_de_las_casillas(2, 2)

  
    def test_turnos_alternan_varias_jugadas(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.assertEqual(juego.turno, "O")
        juego.ocupar_una_de_las_casillas(1, 1)  # O
        self.assertEqual(juego.turno, "X")
        juego.ocupar_una_de_las_casillas(2, 2)  # X
        self.assertEqual(juego.turno, "O")

    def test_gana_o_en_columna(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0)  # X
        juego.ocupar_una_de_las_casillas(0, 1)  # O
        juego.ocupar_una_de_las_casillas(1, 0)  # X
        juego.ocupar_una_de_las_casillas(1, 1)  # O
        juego.ocupar_una_de_las_casillas(2, 2)  # X
        juego.ocupar_una_de_las_casillas(2, 1)  # O -> gana
        self.assertTrue(juego.juego_terminado)
        self.assertEqual(juego.ganador, "O")

if __name__ == "__main__":
    unittest.main()
