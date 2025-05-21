import random
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')
n = int(input('Em que numero eu pensei?'))
print('Processando...')
n1 = random.randint(0,5)
if n == n1:
    print('Você acertou, eu pensei no numero {}'.format(n1))
else:
    print('Você errou, eu pensei no numero {}'.format(n1))
print('Fim do jogo')