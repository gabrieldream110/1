# Desafio 008: Crie um programa que leia uma medida em metros e o converta para centímetros e milímetros.

while (True):

      m  = float(input('Medida em metros:  '))
      #um = input('Unidade de medida:  ')

      polegada      = m*39.37
      milha         = m*0.62137
      jarda         = m*0.9144
      leguasesmaria = m*0.0001515151
      leguamaritima = m*0.0001800002


      km  = m/1000
      he  = m/100
      dam = m/10
      me  = m*1
      d   = m*10
      c   = m*100
      mm  = m*1000

      print('A medida {} m tem:\n'
            '{} kilômetros\n'
            '{} hectômetros\n'
            '{} decâmetros\n'
            '{} metros\n'
            '{} decímetros\n'
            '{} Centímetros\n'
            '{} Milímetros\n\n'.format(m,km,he,dam,me,d,c,mm))

      print('A medida {} m equivale a :\n'
            '{} polegadas.\n'
            '{} milhas.\n'
            '{} jardas.\n'
            '{:.5f} leguas sesmarias.\n'
            '{:.5f} leguas maritimas.\n\nFim!'.format(m,polegada,milha,jarda,leguasesmaria,leguamaritima))

