def calcular_juros_compostos(principal, taxa, tempo):
        return principal * (1 + taxa) ** tempo



def calcular_juros_compostos_recursivo(principal, taxa, tempo):
    if tempo == 0:
        return principal  # Base da recursão
    else:
        return calcular_juros_compostos_recursivo(principal * (1 + taxa), taxa, tempo - 1)


def test():
  assert calcular_juros_compostos(1000, 0.05, 5) == 1276.2815625000003
  assert calcular_juros_compostos(1000, 0.05, 10) == 1628.894626777442
  assert calcular_juros_compostos(1000, 0.05, 0) == 1000

  assert calcular_juros_compostos_recursivo(1000, 0.05, 5) == 1276.2815625000003
  assert calcular_juros_compostos_recursivo(1000, 0.05, 10) == 1628.894626777442
  assert calcular_juros_compostos_recursivo(1000, 0.05, 0) == 1000
