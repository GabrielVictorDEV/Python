#Entrada do numero de itens
itens = int(input("Digite a quantidade de itens que você consumiu? "))
print("")
soma = 0

#Loop da soma dos itens
for i in range(1, itens + 1):
  print("")
  valores = int(input(f"Qual o valor do item {i}? "))
  soma = soma + valores 

#Pergunta da forma de pagamento 
print("")
print("Qual sua forma de pagamento?")
pagamento = int(input("Digite 1 para 'a vista', e 2 para 'crédito': "))

#Escolha da forma de pagamento 
if pagamento == 1:
  valor_final = soma - (soma * 0.05) 
  print("")
  print(f"O seu valor total foi de '{soma}'")
  print("A sua forma de pagamento foi 'a vista'")
  print(f"O seu valor com desconto foi '{soma} - 5% = {valor_final}'")
  print(f"O valor a ser pago foi de: '{valor_final}'")
elif pagamento == 2:
  valor_final = soma - (soma * 0.02) 
  print("")
  print(f"O seu valor total foi de '{soma}'")
  print("A sua forma de pagamento foi 'crédito'")
  print(f"O seu valor com desconto foi '{soma} - 2% = {valor_final}'")
  print(f"O valor a ser pago foi de: '{valor_final}'")
else:
  print("[ERRO], valores inseridos não são validos.")