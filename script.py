def calcular_total(quantidade, valor_unitario):
    return quantidade * valor_unitario


def validar_pedido(item, quantidade, valor_unitario):
    if item and quantidade and valor_unitario:
        return "Pedido Válido"
    else:
        return "Pedido Inválido"