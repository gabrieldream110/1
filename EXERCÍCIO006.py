# Desafio 006: Crie um algoritmo que leia um número e mostre na tela seu dobro, triplo e raiz quadrada:

import math

n = float(input('Digite um valor:'))
d = n * 2
t = n * 3
r = math.sqrt(n)

print('Em relação ao número {}:\n'
      'Seu dobro é {}\n'
      'Seu triplo é {}\n'
      'Sua raíz quadrada é igua a {}\nFim!'.format(n,d,t,r))
