# Desafio 018: Faça um programa que leia um ângulo qualquer e mostre na tela:
# o valor do seno, cosseno e tangente desse ângulo.

import math

a   = float(input('Ângulo de um triângulo:'))
ang = math.radians(a)

s   = math.asin(ang)
c   = math.acos(ang)
t   = math.atan(ang)

print('\n\nPara um ângulo de {}°:\n'
      'Seno:{:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}'.format(a,s,c,t))
