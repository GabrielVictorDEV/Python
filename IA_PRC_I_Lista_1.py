#QUESTÃO 01 ------------------------------------------------------------------------------------

input('Qual seu nome?')
valor = int(input("Digite um valor e descubra seu antecessor! "))
valor_antecessor = valor - 1
print("Seu valor antecessor é: ", valor_antecessor)

#QUESTÃO 02 ------------------------------------------------------------------------------------

salario_mensal = int(input("Digite o valor do seu salário! "))
percentual_de_reajuste = int(input("Digite a porcentagem do seu ajuste "))

percentual = percentual_de_reajuste / 100
valor_percentual = salario_mensal * percentual
valor_inteiro = valor_percentual + salario_mensal

print("O valor do seu reajuste é:", valor_percentual)
print("O valor do seu salario reajustado é: ", valor_inteiro)

#QUESTÃO 03 ------------------------------------------------------------------------------------

ano_de_nascimento = int(input("Qual o seu ano de nascimento? "))
idade = 2022 - ano_de_nascimento
anos_faltantes = 16 - idade

if idade >= 16:
  print("Parabéns, você está apto a votar!")
else: 
  print("Você ainda não possui a idade necessária para votar! Faltam",anos_faltantes, "anos")

#QUESTÃO 04 ------------------------------------------------------------------------------------

valores = []

for c in range (1, 4):
  valores.append(int(input(f"Digite o seu {c}° valor: ")))

valores_ordenados = sorted(valores)
resultado = valores_ordenados[1] + valores_ordenados[2]

print(f"A soma dos maiores números é: {resultado}")

#QUESTÃO 05 ------------------------------------------------------------------------------------ 

primeiro_lado = int(input("Digite o valor do 1° lado: "))
segundo_lado = int(input("Digite o valor do 2° lado: "))
terceiro_lado = int(input("Digite o valor do 3° lado: "))

if (terceiro_lado < primeiro_lado + segundo_lado) and (segundo_lado < primeiro_lado + terceiro_lado) and ( primeiro_lado < terceiro_lado + segundo_lado):
  print("Os valores formam um triângulo")
else: 
  print("Os valores não formam um triângulo.")
  
#QUESTÃO 06 ------------------------------------------------------------------------------------

apples_number = int(input("Quantas maçãs você comprou?"))

if apples_number >= 12:
  duzia = apples_number * 1
  print(f"O valor das suas maçãs é {duzia}")
else:
  duzia = apples_number * 1.30
  print(f"O valor das suas maçãs é {duzia}")
  
#QUESTÃO 07 ------------------------------------------------------------------------------------

name_time_1 = input("Qual o nome do seu primeiro time? ")
gols_1 = int(input("Qual a quantidade de gols? "))

name_time_2 = input("Qual o nome do seu segundo time? ")
gols_2 = int(input("Qual a quantidade de gols? "))

if gols_1 > gols_2:
  print(f"O time {name_time_1} venceu o time{name_time_2}, por {gols_1} x {gols_2}")
elif gols_1 == gols_2:
  print("Não ouve vencedores, ocorreu um EMPATE!")
else:
  print(f"O time {name_time_2} venceu o time {name_time_1}, por {gols_2} x {gols_1}")
  
#QUESTÃO 08 ------------------------------------------------------------------------------------

primeira_nota = float(input("Qual a sua primeira nota? "))
segunda_nota = float(input("Qual a sua segunda nota? "))
terceira_nota = float(input("Qual a sua terceira nota? "))
media_de_exercicios = float(input("Qual a sua média de exercícios? "))

media_de_aproveitamento = float((primeira_nota + (segunda_nota * 2) + (terceira_nota * 3) + media_de_exercicios) / 7)

if media_de_aproveitamento >= 9 and media_de_aproveitamento <= 10:
  print(f"Parabéns, sua media foi de {media_de_aproveitamento:.1f} com o conceito A. :)")
elif media_de_aproveitamento >= 7.5 and media_de_aproveitamento < 9:
  print(f"Parabéns, sua media foi de {media_de_aproveitamento:.1f} com o conceito B. ")
elif media_de_aproveitamento >= 6 and media_de_aproveitamento < 7.5:
  print(f"Parabéns, sua media foi de {media_de_aproveitamento:.1f} com o conceito C. ")
elif media_de_aproveitamento < 6: 
  print(f"Sua media foi de {media_de_aproveitamento:.1f}. Você foi reprovado! com conceito D. :(")
else:
  print("[ERRO] Valores Incorretos, digite apenas entre 0 e 10")
  
#QUESTÃO 09 ------------------------------------------------------------------------------------

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
  
#QUESTÃO 10 ------------------------------------------------------------------------------------
  
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