import unittest
from app import calcular_operacao

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        resultado = calcular_operacao(5, 3, "Soma")
        self.assertEqual(resultado, 8)

    def test_subtracao(self):
        resultado = calcular_operacao(5, 3, "Subtração")
        self.assertEqual(resultado, 2)

    def test_multiplicacao(self):
        resultado = calcular_operacao(5, 3, "Multiplicação")
        self.assertEqual(resultado, 15)

    def test_divisao(self):
        resultado = calcular_operacao(6, 3, "Divisão")
        self.assertEqual(resultado, 2)

    def test_divisao_por_zero(self):
        resultado = calcular_operacao(6, 0, "Divisão")
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
