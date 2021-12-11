# Desafio 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l    = float(input('Digite o valor da largura de uma parede:'))
al   = float(input('Digite o valor da altura dessa parede:'))

area = al * l

t    = area / 2

print('Para uma área de {} m² será necessário {} L de tinta.'.format(area,t))
