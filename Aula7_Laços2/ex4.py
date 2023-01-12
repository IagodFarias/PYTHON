#leia um número e calcule o seu fatorial
#número fatorial: ex.: 4! = 4 x 3 x 2 x 1
#                      n! = n x (n-1) x (n-2) x ... x n-(n-2) x n-(n-1)


num = int(input("digite um número: "))
cont = 1
resultado = num
while cont != num:
    resultado = resultado * (num - cont)
    cont = cont + 1
print(resultado)