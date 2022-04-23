#QUESTÃO 10: Um mercado está vendendo frutas com a seguinte tabela de até 5kg, morango 2 e maça 1,50. Acima de 5kg morango 1,80 maçã 1,10 Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = int(input("Quantos morangos você quer comprar? "))
maca = int(input("Quantas maçãs você quer comprar? "))

def morango_calculo(morango):
  if morango <= 5 and morango >= 1: #Morango
    valor_morango = morango * 2
    print(f"Você deve pagar {valor_morango} pelos morangos.")
  elif morango > 5 and morango <= 8:
    valor_morango = morango * 1.80
    print(f"Você deve pagar {valor_morango} pelos morangos.")
  elif morango > 8:
    valor_morango = morango * 1.80 
    valor_por_cento = (valor_morango * 0.10)
    valor_final = valor_morango - valor_por_cento
    print(f"Você deve pagar {valor_final} pelos morangos.")
  else:
    print("[ERRO], Digite um valor válido!")

def maca_calculo(maca):
  if maca <= 5 and maca >= 1: #Maçã
    valor_maca = maca * 1.50
    print(f"Você deve pagar {valor_maca} pelas maçãs.")
  elif maca > 5 and maca <= 8:
    valor_maca = maca * 1.10
    print(f"Você deve pagar {valor_maca}")
  elif maca > 8:
    valor_maca = maca * 1.10 
    valor_por_cento = (valor_maca * 0.10)
    valor_final = valor_maca - valor_por_cento
    print(f"Você deve pagar {valor_final}")
  else:
    print("[ERRO], Digite um valor válido!")

#chama as funções

morango_calculo(morango)
maca_calculo(maca)