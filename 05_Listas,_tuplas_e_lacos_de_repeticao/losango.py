def desenha_losango(altura):
  altura = int(input("Digite um valor ímpar para a altura do losango: "))
  if altura % 2 == 0:
      altura = altura + 1
      
  meio = altura // 2
  for linha in range(altura):
      if linha <= meio:
          espacos = meio - linha
          estrelas = linha * 2 + 1 
      else: 
          espacos = linha - meio
          estrelas = altura - (linha - meio) * 2
      print(' ' * espacos + '#' * estrelas)


