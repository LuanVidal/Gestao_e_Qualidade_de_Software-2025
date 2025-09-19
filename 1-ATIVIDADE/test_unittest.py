import unittest
from calculadora import somar

class TestCalculadora(unittest.TestCase):

    def test_soma_de_numeros_positivos(self):
        """Testa a soma de dois números positivos."""
        self.assertEqual(somar(2, 3), 5)

    def test_soma_de_numeros_negativos(self):
        """Testa a soma de dois números negativos."""
        self.assertEqual(somar(-1, -1), -2)

    def test_soma_de_positivo_com_negativo(self):
        """Testa a soma de um número positivo com um negativo."""
        self.assertEqual(somar(5, -3), 2)