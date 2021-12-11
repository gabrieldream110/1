# Desafio 016: Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.

from math import trunc
n = float(input('Digite um valor qualquer:'))

print('A porção inteira de {}{}{} é igual a {}{}{}'.format('\033[31m',n,'\033[m','\033[32m',trunc(n),'\033[m'))
