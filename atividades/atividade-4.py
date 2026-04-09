# Peça um valor inteiro positivo ao usuário e determine quantas cédulas de R$100,
# R$50, R$20, R$10, R$5 e R$1 são necessárias para formar esse valor, utilizando
# estruturas de repetição.

valor = int(input("Insira o valor do saque: "))

saque = valor

nota100 = 0 
nota50 = 0 
nota10 = 0 
nota20 = 0 
nota5 = 0 
moeda1 = 0 

while valor != 0:

    if valor > 100:
        valor = valor - 100
        nota100 = nota100 + 1
   
    elif valor < 100 and valor > 50:
        valor = valor - 50
        nota50 = nota50 + 1
   
    elif valor < 50 and valor > 20:
        valor = valor - 20
        nota20 = nota20 + 1
    
    elif valor < 20 and valor > 10:
        valor = valor - 10
        nota10 = nota10 + 1
    
    elif valor < 10 and valor >= 5:
        valor = valor - 5
        nota5 = nota5 + 1
    else:
        valor = valor - 1
        moeda1 = moeda1 + 1

print(f"O seu saque de {saque} reais foi feito com êxito. Voce receberá {nota100} notas de 100 reais, {nota50} notas de 50 reais, {nota20} notas de 20 reais, {nota10} notas de 10 reais, {nota5} notas de 5 reais e {moeda1} moedas de 1 real.")
    