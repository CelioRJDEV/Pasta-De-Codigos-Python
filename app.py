
#Bibliotecas
from datetime import datetime
import random

print('---------- Seja Bem Vindo a nossa empresa !!! ----------')

#Variaveis
nome_user = input("Qual é seu nome? ")
idade_user = int(input("Qual é sua idade? "))
data_cadastro = datetime.now()
aniversario = datetime.strptime(
    input('Digite a data do seu aniversario no farmato dd/mm/aaaa: '),"%d/%m/%Y")
cartoes = ['R$50,00','R$250,00','R$120,00']
cartao = random.choice(cartoes)


print(f'Olá {nome_user}, seu registro foi conluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}.
    \nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}')