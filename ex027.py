nome1 = str(input('Digite seu nome completo:')).strip()
nome2 = nome1.split()[0]
nome3 = nome1.split()[-1]
print('primeiro nome: {} \nUltimo nome: {}'.format(nome2, nome3))
