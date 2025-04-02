ANO_ATUAL = 2025
nome = input('Qual o seu nome?')
sobrenome = input('Qual o seu sobrenome?')
ano_nascimento = int(input('Que ano você nasceu?'))
idade = ANO_ATUAL - ano_nascimento
print('olá', nome, sobrenome, 'Bom dia, sua idade é', idade)
