from script import calcular_total
from script import validar_pedido
import pytest

def test_calcular_total():
    assert calcular_total(2,5) == 10


def test_validar_pedido():
    assert validar_pedido("Coxinha", 2, 3) == "Pedido Válido"


# Testes errados
def test_validar_pedido_item_invalido():
    assert validar_pedido("", 2, 3) == "Pedido Inválido: Item inválido"


def test_validar_pedido_quantidade_invalido():
    assert validar_pedido("Coxinha", 0, 3) == "Pedido Inválido: Quantidade inválida"


def test_validar_pedido_valor_unitario_invalido():
    assert validar_pedido("Coxinha", 3, 0) == "Pedido Inválido: valor unitario inválido"
