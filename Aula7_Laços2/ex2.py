from random import randint
num = randint(1,10)
flag = -1
while flag != 0:
    num2 = int(input(""))
    if num == num2:
        print("*=" * 20)
        print("Voce acertou: \ncpu = {} \njogado = {}".format(num, num2))
        print("*=" * 20)
        flag = 0
    else: 
        print("*=" * 20) 
        print("Vc errou") 
        print("*=" * 20)
