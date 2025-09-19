from calculadora import somar

def test_soma_de_numeros_positivos():
    """Testa a soma de dois números positivos."""
    assert somar(2, 3) == 5

def test_soma_de_numeros_negativos():
    """Testa a soma de dois números negativos."""
    assert somar(-1, -1) == -2

def test_soma_de_positivo_com_negativo():
    """Testa a soma de um número positivo com um negativo."""
    assert somar(5, -3) == 2