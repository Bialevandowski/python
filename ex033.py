n1 = int(input('Digite o 1 valor:'))
n2 = int(input('Digite o 2 valor:'))
n3 = int(input('Digite o 3 valor:'))
print('Validando números...')
if n1 < n2 and n1 < n3:
    print('o número {} é o menor!'.format(n1))
elif n2 < n1 and n2< n3:
    print('O número {} é o menor!'.format(n2))
elif n3< n1 and n3 < n2:
    print ('O número {} é o menor!'.format(n3))
if n1 > n2 and n1 > n3:
     print('O número {} é o maior!'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O número {} é o maior!'.format(n2))
elif n3 > n1 and n3 > n2:
    print ('O número {} é o maior!'.format(n3))
print('Até a proxima ')
