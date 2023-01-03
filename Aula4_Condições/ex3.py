#leia um número e descubra se ele é par ou é ímpar

num = int(input("Digite um número: "))
if num % 2 == 0:
    print("o {} é par!".format(num))
else: print("o {} é ímpar".format(num))