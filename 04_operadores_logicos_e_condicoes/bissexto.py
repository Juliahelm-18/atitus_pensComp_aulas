def eh_bissexto(ano):
   if ano % 4 == 0:
       return True
   else:
       return False
def proximo_bissexto(ano):
   return not eh_bissexto(ano):

def verificar_bissexto(ano):
  ano = input("Digite um ano")
   if ano % 4 == 0:
      return True
      print("O ano é bissexto")
   if ano % 4 == 3:
      return (ano + 1) True
      print("O ano (ano + 1) será bissexto")
   if ano % 4 == 2:
       return (ano + 2) True
      print("O ano (ano + 2) será bissexto")
   if ano % 4 == 1:
      return (ano + 3) True
      print("O ano (ano + 3) será bissexto")
   

def test():
assert eh_bissexto(0)
assert eh_bissexto(2020)
assert eh_bissexto(2024)

assert not eh_bissexto(1)
assert not eh_bissexto(2022)
assert not eh_bissexto(2023)

assert proximo_bissexto(2024) == 2024
assert proximo_bissexto(2025) == 2028
assert proximo_bissexto(2029) == 2032
assert proximo_bissexto(2020) == 2020
