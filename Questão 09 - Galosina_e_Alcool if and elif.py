##QUESTÃO 09: Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#• Álcool: até 20 litros, desconto de 3% por litro.
#• Álcool: acima de 20 litros, desconto de 5% por litro.
#• Gasolina: até 20 litros, desconto de 4% por litro.
#• Gasolina: acima de 20 litros, desconto de 6% por litro.
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: Álcool, Gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço da gasolina é de R$ 1,20 o litro e o álcool R$ 0,90.

print("Qual combustivel você prefere? ")
combustivel_tipo = int(input("Digite 1 para Alcool ou 2 para Gasolina: "))
combustivel_quantidade = int(input("Quantos litros você vai querer? "))

if combustivel_tipo == 1: # calculo Álcool 
  if combustivel_quantidade < 20 and combustivel_quantidade >= 1: #Abaixo de vinte
    desconto = (0.90 * 0.03) * combustivel_quantidade
    combustivel_desconto = (combustivel_quantidade * 0.90) - desconto
    print(f"O valor do seu combustivel ficou de {combustivel_desconto:.2f}R$, por {combustivel_quantidade} litros.")
  elif combustivel_quantidade >= 20: #Acima de vinte
    desconto = (0.90 * 0.05) * combustivel_quantidade
    combustivel_desconto = (combustivel_quantidade * 0.90) - desconto
    print(f"O valor do seu combustivel ficou de {combustivel_desconto:.2f}R$, por {combustivel_quantidade} litros.")
  else: 
    print("[ERRO] O valor inserido, precisa ser maior que zero!")
elif combustivel_tipo == 2: #calculo Gasolina 
  if combustivel_quantidade < 20 and combustivel_quantidade >= 1: #Abaixo de vinte
    desconto = (1.20 * 0.04) * combustivel_quantidade
    combustivel_desconto = (combustivel_quantidade * 1.20) - desconto
    print(f"O valor do seu combustivel ficou de {combustivel_desconto:.2f}R$, por {combustivel_quantidade} litros.")
  elif combustivel_quantidade >= 20: #Acima de vinte
    desconto = (1.20 * 0.06) * combustivel_quantidade
    combustivel_desconto = (combustivel_quantidade * 1.20) - desconto
    print(f"O valor do seu combustivel ficou de {combustivel_desconto:.2f}R$, por {combustivel_quantidade} litros.")
  else: 
    print("[ERRO] O valor inserido, precisa ser maior que zero!")
else:
  print("Digite um combustivel e valor valido!")