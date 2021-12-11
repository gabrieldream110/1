# Desafio 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d  = float(input('Dias alugados pelo cliente:'))
k  = float(input('Quilometragem total rodada pelo cliente:'))

dt = d * 60
kt = k * 0.15
vt = dt + kt

print('Total de dias alugados:  {}{}{} = R$ {}{}{}\n'
      'Total de KM rodados:    {}{}{} = R$ {}{}{}\n'
      'Valor a ser cobrado:           R$ {}{}{}'
      .format('\033[36m',d,'\033[m','\033[32m',dt,'\033[m','\033[35m',k,'\033[m','\033[32m',kt,'\033[m',
              '\033[32m',vt,'\033[m'))
