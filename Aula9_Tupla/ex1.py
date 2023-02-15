lista = 'zero','um','dois','três', 'quatro', 'cinco', 'seis','sete', 'oito', 'nove', 'dez'

while True:
    flag = int(input('digite um número entre zero e dez: '))
    if flag > 0 and flag <= 10:
        print(f'Voce digitou o número {lista[flag]}')
        break
    else: 
        print('tente novamente. Digite um número entre zero e dez') 