numero = str(input('Digite um numero de 0 a 9999:'))
numero = numero.zfill(4)
u = numero[3]
d = numero[2]
c = numero[1]
m = numero[0]
print(' Unidade:{}\n Dezena:{} '
      '\n Centena:{}\n Milhar:{}'.format(u,d,c,m))



