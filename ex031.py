km = float(input('Quantos kilometros da a sua viagem?'))
if km <= 200:
    custo = km *0.50
    print('Sua viagem custa R${}'.format(custo))
else:
    custo1 = km * 0.45
    print('A sua viagem custa R${}'.format(custo1))
print('Boa viagem!')