#jogo de adivinhação: o computador pensa em um número de 0 a 5 e vc tenta acertar

import random
print("Escolhi um número entre 0 e 5")
x = random.randrange(1,5)
num = float(input("adivinhe o número: "))
if x == num:
    print("você acertou o número")
else: print("vc não acertou o número, ele era {}".format(x))


