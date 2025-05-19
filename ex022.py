nome = str(input('Digite seu nome completo:'))
print(nome.upper())
print(nome.lower())
letras = (len(nome))
espaco = (nome.count(' '))
total= letras - espaco
print('A quantia de caracteres que tem é :{}'.format(total))
dividido = nome.split()
print(dividido[0])
