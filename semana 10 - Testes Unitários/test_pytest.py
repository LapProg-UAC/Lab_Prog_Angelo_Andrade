import pytest
from funcao_doctest import gerar_f


def test_cinco():
    """Primeiros 5 termos devem corresponder à sequência definida."""
    assert gerar_f(5) == [0, 1, 1, 4, 7]


def test_zero():
    """f(0) deve devolver [0]."""
    assert gerar_f(0) == [0]


def test_negativo():
    """Valores negativos devem gerar ValueError."""
    with pytest.raises(ValueError):
        gerar_f(-1)


def test_tipo_invalido():
    """Tipos inválidos devem gerar ValueError."""
    with pytest.raises(ValueError):
        gerar_f("abc")
