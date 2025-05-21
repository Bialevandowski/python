s = float(input('Digite o seu salario:'))
if s >= 1250:
    a1 = s * 0.10
    a2 = a1 + s
    print('O seu novo salario é de R${:.2f}'.format(a2))
else:
    a3 = s * 0.15
    a4 = a3 + s
    print('O seu novo salario é de R${:.2f}'.format(a4))
print('Felicidades pelo novo salario!')