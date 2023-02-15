times = ('palmeira', 'internacional', 'fluminense', 'corinthias', 'flamengo','athletico-PR', 'atlético-MG', 'fortaleza', 'são paulo', 'américa-MG')

print("Os cinco primeiro colocados são: ")
for pos in range(0,5):    
    print(f'{times[pos]} na {pos + 1}º posição') 
print('-*'* 40)

print('Os quatro últimos colocados são: ')
for c in range(6, 10):
    print(f'{times[c]} na {c+ 1}º posição ')

print('-*'* 40)

time_ord = sorted(times)
for c in range(0, len(times)):
    print(f'{time_ord[c]}')

print('-*'* 40)

print(f'O Fortaleza está na {times.index("fortaleza") + 1}º posição')


