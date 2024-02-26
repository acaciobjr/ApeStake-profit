import datetime

deposito = float(input("Digite o valor de depósito no Ape Stake\nque você deseja saber o montante \nao final do ano de 2023:  "))

data_atual = datetime.date.today()
ano_atual = data_atual.year
data_final = datetime.date(ano_atual, 12, 31)
print('a data atual é:', data_atual)

dias_restantes = (data_final - data_atual).days
print('hoje faltam', dias_restantes ,'dias para acabar o ano')

taxa_juros = 0.68
print('O valor de APR do ApeStake para o ano de 2023 é de:', taxa_juros*100,'%')
montante = deposito * (1 + taxa_juros) ** (dias_restantes / 365)
print('O montante ao final do ano será de R$', round(montante, 2))
