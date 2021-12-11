# Desafio 013: Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

while (True):

    s   = float(input('Digite o valor de salário de um funcionário:'))
    p   = float(input('Digite o percentual do reajuste:'))
    q   = input('O reajuste é de aumento? Senão, será considerado reajuste de redução. Digite: sim ou não')

    vp  = s * (p/100)
    aum = s + vp
    red = s - vp

    if q == 'sim':
        print('\033[32mPara um salário de R$ {}, cujo aumento será de {}%, terá valor final de remuneração igual a:\n'
              'R$ {}.\033[m'.format(s,p,aum))
    else:
        print('\033[31mPara um salário de R$ {}, cujo valor será reduzido em {}%, terá valor final de remuneração'
              ' igual a :\nR$ {}.\033[m'.format(s,p,red))
