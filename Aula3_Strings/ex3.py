# leia um número no intervalo [0,1000] e diga quantoas unidades, dezenas, centenas e milhares de unidades ele tem.
num = int(input("digite um número: "))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(" a unidade é {} \n a dezena é {}\n a centena é {}\n o milhar é {} ".format(u, d, c, m))
