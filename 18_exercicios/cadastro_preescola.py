IDADE_PARA_MAIORIDADE = 18


def verifica_maioridade(idade: int) -> bool:
    if idade >= IDADE_PARA_MAIORIDADE:
        return True
    else:
        return False


def verifica_email(email: str) -> bool:
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None


def solicita_nome() -> str | None:
    nome = input("Digite seu nome: ").strip()
    return nome if nome else None



def test():
  assert not verifica_maioridade(-1)
  assert not verifica_maioridade(0)
  assert not verifica_maioridade(1)
  assert not verifica_maioridade(17)
  assert verifica_maioridade(18)
  assert verifica_maioridade(20)
  assert verifica_maioridade(100)


  assert not verifica_email('')
  assert not verifica_email('@')
  assert not verifica_email('@@')
  assert not verifica_email('abc@@abc.com')
  assert not verifica_email('abc@abc.edu')
  assert not verifica_email('a_b_c@a_b_c.com.com')
  assert not verifica_email('a_b_c@a_b_c.com.com.com')

  assert verifica_email('ABC@a_b_c.com')
  assert verifica_email('ABC@ABC.com')
  assert verifica_email('AbC@1BC.com')
  assert verifica_email('abc@abc.com')
  assert verifica_email('a23@123.com')
  assert verifica_email('a_b_c@a_b_c.com')
