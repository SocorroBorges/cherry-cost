from decimal import Decimal

def calcular_custo_total(lista_materiais):
    total = Decimal("0.00")
    for item in lista_materiais:
        custo = item["quantidade"] * item["custo_unitario"]
        total += custo
    return total


def calcular_preco_sugerido(custo_total, margem_percentual):
    return custo_total + (custo_total * margem_percentual / Decimal("100"))