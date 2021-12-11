# Desafio 005: Crie um programa que leia um número e mostre seu sucessor e seu antecessor:

n  = int(input('Digite um valor:'))
n1 = 1
a  = n - n1
s  = n + n1

print('Em relação ao valor {}:\nSeu antecessor é {}\nSeu sucessor é {}\nFim!'.format(n,a,s))
