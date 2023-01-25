
soma = 0
flag = 0
while flag != 999:
    numero = int(input(""))
    flag += 1
    if numero == 999:
        break
    else: soma = soma + numero
    
print(f'foram digitados {flag - 1} números')
print(f'a soma dos números digitados é {soma}')
