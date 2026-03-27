from script import calcular_total
from script import validar_pedido
import pytest

def test_calcular_total():
    assert calcular_total(2,5) == 10


def test_validar_pedido():
    assert validar_pedido("Coxinha", 2, 3) == "Pedido Válido"



