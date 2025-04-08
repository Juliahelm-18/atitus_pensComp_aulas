def senha(palpite):
  palpite = int(input("Digite um número entre 0 e 10"))
  senha = 4
  tentativas = 0
  while senha != palpite:
    print("Senha errada")
    palpite = int(input("Digite um número entre 0 e 10"))
    tentativas += 1
  print("Você acertou a senha!")
  print(f"Essas foram suas tentativas {tentativas}")



