lista_de_frutas = []
i = 0
while i < 5:
  fruta = input('Escreva o nome de uma fruta:  ')
  lista_de_frutas.append(fruta)
  i =+1
  if fruta == "sair":
    lista_de_frutas.pop()
    break
  
print(lista_de_frutas)
def preco_das_frutas(frutas):
  lista_de_preco = []
  i =0
  while  i < 5 :
    valor = float(input("Digite o preço da fruta: "))
    i += 1
    if valor == 0:
      break
    lista_de_preco.append(valor)
  print(lista_de_frutas,lista_de_preco)
preco_das_frutas(len(lista_de_frutas))
