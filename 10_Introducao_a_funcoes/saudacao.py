def saudacao(nome, sobrenome, titulo='Prof'):
    if titulo is None:
        print('Olá Sr.' nome + sobrenome)
    else:
        print('Olá' titulo + nome + sobrenome)


def test():
  assert saudacao("Matheus") == "Olá, Sr. Matheus"
  assert saudacao("Matheus", "Jardim") == "Olá, Sr. Matheus Jardim"
  assert saudacao("Matheus", "Jardim", "Prof") == "Olá, Prof Matheus Jardim"
  assert saudacao("Matheus", titulo="Prof") == "Olá, Prof Matheus"
  assert saudacao("") == "Olá!"
