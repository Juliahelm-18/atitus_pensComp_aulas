def eh_bissexto(ano):
   if ano % 4 == 0:
      print('O ano é bissexto')
      return True
   else:
       print('O ano não é bissexto')
      return False

def proximo_bissexto(ano):
  ano = input("Digite um ano")
    if ano % 4 == 0:
       print("O ano é bissexto")
    if ano % 4 == 3:
       print("O ano (ano + 1) será bissexto")
       ano += 1
    if ano % 4 == 2:
       print("O ano (ano + 2) será bissexto")
       ano += 2
    if ano % 4 == 1:
       print("O ano (ano + 3) será bissexto")
       ano += 3
   

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

# Solucao do Professor
def proximo_bissexto(ano):
   return (ano + 3) // 4 * 4
