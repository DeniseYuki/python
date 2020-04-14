Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
print('-'*30)
nome = input('Digite seu nome: ')
def jogo():
    print('-'*30)
    escolha = input('Qual será sua escolha pedra, papel ou tesoura?:   ')
    print('-'*30)
    lista = ['pedra', 'papel', 'tesoura']
    a = random.choice(lista)
    pontoE = 0
    pontoA = 0
    if a == 'pedra' and a != escolha:
        if escolha == 'papel':
            print('%s você ganhou!'%nome)
            pontoE == 1
            pontoE += 1
        else:
            print('%s você perdeu!'%nome)
            pontoA == 1
            pontoA += 1
    if a == 'papel' and a != escolha:
        if escolha == 'tesoura':
            print('%s você ganhou!' %nome)
            pontoE == 1
            pontoE += 1
        else:
            print('%s você perdeu!'%nome)
            pontoA == 1
            pontoA += 1
    if a == 'tesoura' and a != escolha:
        if escolha == 'pedra':
            print('%s você ganhou!' % nome)
            pontoE == 1
            pontoE += 1
        else:
            print('%s você perdeu!'%nome)
            pontoA == 1
            pontoA += 1
    if a == escolha:
        print('empate')
    print(nome,':',pontoE,'Computador :',pontoA)
    print('-'*30)
    print('Você escolheu: ',escolha,' o computador escolheu: ',a)

jogo()
continuar = input('[S/N]: ')
while continuar == 's':
    if continuar == 's':
        jogo()
        continuar = input('[S/N]: ')
print('fim de jogo!')
