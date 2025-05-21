radar = float(input('Qual a velocidade que o carro passou no radar?'))
cal = radar - 80
multa = cal * 7.00

if radar > 80:
    print('Você foi multado no valor de {}'.format(multa))
else:
    print('Você passou dentro do limite!')
