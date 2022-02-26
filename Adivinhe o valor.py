# JOGOS DA ADIVINHAÇÃO V2


from random import randint
computador = randint(0,10)
print("---"*22)
print("Olá !!!")
print('Sou seu computador ... Acabei de pensar em um número de: 0 e 10.')
print("---"*22)

print('Será que você consegur adivinhar qual foi?')
print("---"*22)

acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpites:  '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("---"*22)
            print(' Mais... tente mais uma vez')
        elif jogador > computador:
            print("---"*22)
            print('Menos... tente mais uma vez')
            
print("---"*22)
print("---"*22)

print('Parabens!!! Acertou com {} palpites'.format(palpite))

print("---"*22)
print("---"*22)