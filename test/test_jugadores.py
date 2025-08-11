import unittest
from jugadores import Jugador

class TestJugador(unittest.TestCase):
    def test_crear_jugador(self):
        j = Jugador("Juan", "X")
        self.assertEqual(j.nombre, "Juan")
        self.assertEqual(j.ficha, "X")

    def test_repr_simple(self):
        j = Jugador("Maria", "O")
        texto = repr(j)
        self.assertIn("Maria", texto)
        self.assertIn("O", texto)

    # extra: cambiar el nombre a mano (atributo simple)
    def test_cambiar_nombre_manual(self):
        j = Jugador("Ana", "X")
        j.nombre = "Luis"
        self.assertEqual(j.nombre, "Luis")

if __name__ == "__main__":
    unittest.main()
