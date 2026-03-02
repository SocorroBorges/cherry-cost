from decimal import Decimal
from app.services import calcular_custo_total, calcular_preco_sugerido

materiais = [
    {"quantidade": Decimal("2"), "custo_unitario": Decimal("5.50")},
    {"quantidade": Decimal("1"), "custo_unitario": Decimal("3.00")}
]

custo_total = calcular_custo_total(materiais)
preco = calcular_preco_sugerido(custo_total, Decimal("30"))

print("custo total:", custo_total)
print("Preço sugerido:", preco)