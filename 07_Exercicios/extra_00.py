ANO_ATUAL = 2025

def saudacao(nome, sobrenome, ano_nascimento):
    nome = input ("Olá, qual seu nome? ")
    sobrenome = input ("E qual seu sobrenome? ")
    ano_nascimento = int(input("Que ano você nasceu?"))
    idade = ANO_ATUAL - ano_nascimento
    if not (0 <= ano_nascimento < ANO_ATUAL)
        return None
    print (f'Olá,{nome} {sobrenome}. Bom dia! Você possuí {idade} anos!')



def test ():
  assert (saudação("Maheus", "Jardim", 1991) == "Olá, Matheus Jardim. Bom dia! Você possui 33 anos! ")
  assert ( saudacao("Thais", "Silva", 1990) == "Olá, Thais Silva. Bom dia! Você possui 34 anos! ")
  
  assert saudacao("Matheus", "Jardim", 0) is None
  assert saudacao("Matheus", "Jardim", 2050) is None
