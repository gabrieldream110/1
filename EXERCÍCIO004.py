# Desafio 004: Crie um programa que leia uma variável e mostre seu tipo primitivo e mais informações:

x = input('Digite algo:')
print(type(x))
print('O valor {} é numérico?'.format(x),x.isnumeric())
print('O valor {} é alfabético?'.format(x),x.isalpha())
print('O valor {} é alfanumérico?'.format(x),x.isalnum())
print('O valor {} é maiúsculo?'.format(x),x.isupper())
print('O valor {} é minúsculo?'.format(x),x.islower())
print('O valor {} contém só espaços?'.format(x),x.isspace())
print('O valor {} está capitalizado?'.format(x),x.istitle())
