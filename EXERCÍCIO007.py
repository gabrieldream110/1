# Desafio 007: Desenvolva um programa que leia duas notas de um aluno e mostre sua média aritmética:

n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))

m  = (n1 + n2)/2

print('Um aluno, com notas {} e {} terá o seguinte resultado: \n'.format(n1,n2))

if m > 4:
    print('O aluno teve média {}, portanto foi aprovado!'.format(m))
else:
    print('O aluno teve média {}, portanto foi reprovado.'.format(m))
