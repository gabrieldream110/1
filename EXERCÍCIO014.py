# Desafio 014: Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.

c = float(input('Digite o valor de uma temperatura em graus °C:'))
# Fórmula oficial para calcular e converter em Fahrenheit: ((C° x 9)/5) + 32 ou (1.8 x 5) + 32:

f = ((c * 9) / 5) + 32

print('Um elemento à temperatura de {}{}{} °C equivale a:\n'
      '{}{}{} °F'.format('\033[32m',c,'\033[m','\033[31m',f,'\033[m'))
