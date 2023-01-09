#faça um programa que leia número inteiros e verifique se ele é primo ou não
flag = 0
num = int(input(" digite um número: "))
for c in range(1, num):
    rest = num % c
    if rest != 0:
        flag = flag - 1 # se o resto da divisão por C for diferente de zero flag = -1 (sinaliza que é primo)
    else: flag = 0 # se o resto da divisão por C for igual a zero flag = 0 (sinaliza que não é primo)
if flag == -1:
    5
    print("{} é primo".format(num)) #se flag = -1 então sinaliza que é primo
else: print("{} não é primo".format(num)) # se flag = 0 então sinaliza que não é primo
