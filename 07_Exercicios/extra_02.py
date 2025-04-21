def maior_numero(lista):
  escolha = int(input("Escolha qual lista você deseja descobrir o maior número, 1, 2 ou 3: ")
  if escolha < 1 and > 3:
                return None
  if escolha == 1:
    maior_numero = max(lista_1)
    print(f"O maior número é {maior_numero}")
  elif escolha == 2
      maior_numero = max(lista_2)
    print(f"O maior número é {maior_numero}")
  elif escolha == 3
      maior_numero = max(lista_3)
    print(f"O maior número é {maior_numero}")
                


def menor_numero(lista):
  escolha = int(input("Escolha qual lista você deseja descobrir o maior número, 1, 2 ou 3: ")
  if escolha < 1 and > 3:
                return None
  if escolha == 1:
    menor_numero = min(lista_1)
    print(f"O maior número é {maior_numero}")
  elif escolha == 2
      menor_numero = min(lista_2)
    print(f"O maior número é {maior_numero}")
  elif escolha == 3
      menor_numero = min(lista_3)
    print(f"O maior número é {menor_numero}")
 


def numeros_pares(lista):
    # Quais números são pares.
    pass


def numeros_impares(lista):
    # Quais números são ímpares.
    pass


def numeros_positivo(lista):
    # Quais números são positivos
    pass


def numeros_negativos(lista):
    # Quais números são negativos.
    pass


def soma_numeros(lista):
    # A soma de todos os números.
    pass


lista_1 = [10, 0, -3, 42, 5, -6, 8, 91]
lista_2 = [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
lista_3 = [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]
assert maior_numero(lista_1) == 91
assert maior_numero(lista_2) == 95
assert maior_numero(lista_3) == 92

assert menor_numero(lista_1) == -6
assert menor_numero(lista_2) == 2
assert menor_numero(lista_3) == 5

assert numeros_pares(lista_1) == [10, 0, 42, -6, 8]
assert numeros_pares(lista_1) == [20, 2, 74, 22]
assert numeros_pares(lista_1) == [92, 50, 28]

assert numeros_impares(lista_1) == [-3, 5, 91]
assert numeros_impares(lista_1) == [27, 19, 85, 3, 95, 11]
assert numeros_impares(lista_1) == [45, 23, 17, 89, 57, 15, 5]

assert numeros_positivo(lista_1) == [10, 0, 42, 5, 8, 91]
assert numeros_positivo(lista_1) == [20, 2, 27, 74, 19, 85, 3, 22, 95, 11]
assert numeros_positivo(lista_1) == [45, 92, 23, 17, 50, 89, 57, 15, 28, 5]

assert numeros_negativos(lista_1) == [-3, -6]
assert numeros_negativos(lista_1) == []
assert numeros_negativos(lista_1) == []

assert soma_numeros(lista_1) == 147
assert soma_numeros(lista_1) == 358
assert soma_numeros(lista_1) == 421
