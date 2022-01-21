numero_1 = input("Digite um numero: ")

if numero_1.isnumeric() or numero_1.isdecimal():
  numero_1 = int(numero_1)
  if numero_1 % 2 == 0:
    print("Esse numero é par")
  elif numero_1 % 2 != 0:
    print("Esse numero é impar")
else: 
  print("Esse não é um numero")

------------------

hora = input("Digite a hora atual: ")

if hora.isnumeric() and hora.isdecimal(): 
  hora = int(hora)
  if hora >= 0 and hora <= 11:
    print("Bom dia!")
  elif hora >= 12 and hora <= 17:
    print("Boa tarde!")
  elif hora >= 18 and hora <= 23:
    print("Boa noite!")
else:
  print("Valor digitado não é uma hora valida.")

---------------------

nome = input("Digite seu nome: ")
tamanho = len(nome)

if tamanho <= 4:
  print("Seu nome é curto.")
elif tamanho >= 5 and tamanho <= 6:
  print("Seu nome é normal.")
elif tamanho > 6:
  print("Seu nome é muito grande.")