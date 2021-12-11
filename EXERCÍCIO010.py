# Desafio 010: Crie um programa que mostre quanto dinheiro uma pessoa tem na carteira e:
# Calcule quanto dólar essa pessoa pode comprar:

r       =  float(input('Quanto dinheiro você tem na carteira?'))
d       = 5.36
dam     = r/5.36
dau     = r/3.36
dca     = r/3.90
dhkong  = r/0.69
eur     = r/5.94
fsuico  = r/5.58



print('\n\nSe você tem R$ {} na carteira temos que:\n'
      'Com o dólar valendo R$ {}\n'
      'Você pode comprar:\n'
      'U$ {:.2f} dólares americanos.\n'
      'U$ {:.2f} dólares austríacos.\n'
      'U$ {:.2f} dólares canadenses.\n'
      'U$ {:.2f} dólares de hong kong\n'
      'EU {:.2f} euros.\n'
      'F$ {:.2f} francos suíços.\n'
      'Fim!'.format(r,d,dam,dau,dca,dhkong,eur,fsuico))
