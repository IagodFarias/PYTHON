#leia tres números e diga qual o menor deles

n1 = int(input("digite um número : "))
n2 = int(input("digite um número : "))
n3 = int(input("digite um número : "))

menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print("o menor valor de todos é {}".format(menor))