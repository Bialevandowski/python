r1 = float(input('Digite o valor da 1 reta:'))
r2 = float(input('Digite o valor da 2 reta:'))
r3 = float(input('Digite o valor da 3 reta:'))
if r1+ r2 > r3 and r2 + r3 > r3 and r3 + r2 > r1:
    print('Essas 3 retas formam um triangulo!')
else:
    print('Essas 3 retas não formam um triangulo!')
