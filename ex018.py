import math
a = float(input('Digite um angulo:'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('o valor de seno é {:.3f}!\n O valor de cosseno é{:.3f}!'
      ' \n O valor de Tangente é {:.3f}!'.format(s, c, t))