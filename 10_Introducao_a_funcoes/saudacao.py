def saudacao(nome: str , sobrenome: str, titulo: str) -> str:
    if titulo is None:
        return 'Olá, Sr.' + nome + sobrenome
    elif:
        return 'Olá, ' + titulo + nome + sobrenome
    else: 
        return 'Olá, ' + titulo + nome


def test():
  assert saudacao("Matheus") == "Olá, Sr. Matheus"
  assert saudacao("Matheus", "Jardim") == "Olá, Sr. Matheus Jardim"
  assert saudacao("Matheus", "Jardim", "Prof") == "Olá, Prof Matheus Jardim"
  assert saudacao("Matheus", titulo="Prof") == "Olá, Prof Matheus"
  assert saudacao("") == "Olá!"
