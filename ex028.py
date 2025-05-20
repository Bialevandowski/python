import random
n = int(input('Tenta advinhar um numero de 0 a 5!'))
n1 = random.randint(0,5)
if n == n1:
    print('Você acertou!')
else:
    print('Você errou!')
print('Fim do jogo')