import unittest
from funcao_doctest import gerar_f


class TestGerarF(unittest.TestCase):
    """Testes unitários para a função gerar_f()."""

    def test_zero(self):
        """f(0) deve devolver [0]."""
        self.assertEqual(gerar_f(0), [0])

    def test_um(self):
        """f(1) deve devolver [0]."""
        self.assertEqual(gerar_f(1), [0])

    def test_cinco(self):
        """Primeiros 5 termos devem corresponder à sequência definida."""
        self.assertEqual(gerar_f(5), [0, 1, 1, 4, 7])

    def test_negativo(self):
        """Valores negativos devem gerar ValueError."""
        with self.assertRaises(ValueError):
            gerar_f(-1)

    def test_tipo_invalido(self):
        """Tipos inválidos devem gerar ValueError."""
        with self.assertRaises(ValueError):
            gerar_f("abc")


if __name__ == "__main__":
    unittest.main()