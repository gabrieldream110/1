# Desafio 017: Faça um programa que leia o comprimento
# do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import sqrt

co  = float(input('Cateto o posto:'))
ca  = float(input('Cateto adjacente:'))
hi  = sqrt((pow(co,2))+(pow(ca,2)))
hip = ((co**2) + (ca**2))**(1/2)

print('Hipotenusa: {:.2f}'.format(hi))
