ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
idade_para_se_aposentar = int(input('Digite a idade que você quer se aposentar: '))
expectativa_de_vida = int(input('Qual a sua expectativa de vida? '))
patrimonio_atual = int(input('Qual seu patrimonio atual? '))
taxa_anual_cresci_patri = int(input('Qual a taxa anual de crescimento do seu patrimonio? '))
aporte_mensal = int(input('Qual o valor do seu aporte mensal? '))
custo_mensal_aposentadoria = int(input('Qual sera o custo mensal da sua aposentadoria? '))

ANO_ATUAL = 2025
idade_atual = ANO_ATUAL - ano_de_nascimento
ano_que_ira_se_aposentar = ano_de_nascimento + idade_para_se_aposentar
quantos_anos_faltam_aposentadoria = ano_que_ira_se_aposentar - ANO_ATUAL
taxa_de_crescimento_anual = (1 + (taxa_anual_cresci_patri / 100)) ** (1 / 12) - 1
taxa_mensal = 1 + taxa_de_crescimento_anual
meses_para_se_aposentar = idade_para_se_aposentar * 12
ja_aposentado = (expectativa_de_vida - idade_atual) * 12


for mes in range(meses_para_se_aposentar + 12):
    patrimonio_atual = (patrimonio_atual * taxa_mensal ) + aporte_mensal

gasto = expectativa_de_vida - idade_para_se_aposentar

for mes in range(gasto - (ja_aposentado + 1)):
    patrimonio_atual = (mes * taxa_mensal) - custo_mensal_aposentadoria

print (f'Sua herança {patrimonio_atual}')