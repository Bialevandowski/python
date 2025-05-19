frase = str(input('Digite uma frase:'))
nome1 = frase.count('a')
nome2 = frase.count('A')
total = nome1 + nome2
print('A letra A aparece na frase {} vezes! '.format(total))
frase1 = frase.find('a')
print('A primeira posição que a letra a aparece é: {}'.format(frase1))
frase2 = frase.rfind('a')
print('A ultima posição que a letra a aparece é: {}'.format(frase2))
