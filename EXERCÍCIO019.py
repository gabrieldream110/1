# Desafio 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

n1 = input('Primeiro aluno:')
n2 = input('Segundo aluno:')
n3 = input('Terceiro aluno:')
n4 = input('Quarto aluno:')

alunos  = (n1,n2,n3,n4)
sorteio = choice(alunos)

print('O aluno escolhido foi {}{}{}'.format('\033[32m',sorteio,'\033[m'))
