# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

p   = float(input('Digite o valor de um produto:'))
por = float(input('Determine a porcentagem:'))
q   = input('Escolha e digite: desconto ou aumento?')
de  = p*(por/100)

vfd = p - de

vfa = p + de

if q == 'desconto':
    print('Para um produto de valor {} seu desconto será de:\n\n'
          'R$ {}'.format(p,vfd))
else:
    print('Para um produto de valor {} seu aumento será de:\n\n'
          'R$ {}.\n\nFim!'.format(p,vfa))
