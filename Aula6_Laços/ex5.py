#faça um programa que leia número inteiros e verifique se ele é primo ou não
flag = 0 # O número é considerado primo desde o início
num = int(input("digite um número: "))
for c in range(2, num):
    rest = num % c
    if rest == 0:
        flag = - 1 # se o resto da divisão por C for diferente de zero flag = -1 (sinaliza que é primo)
if flag == 0:
    print("{} é primo".format(num)) #se flag = 0 então sinaliza que é primo
else: print("{} não é primo".format(num)) # se flag = -1 então sinaliza que não é primo
