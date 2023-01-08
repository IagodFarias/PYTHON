
num = int(input("Digite um número: "))
s = 0

print("-=" * 20)
for c in range(0,10):
    tabuada = num * (s+c)
   
    print("{} x {} = {} ".format(num,s+c, tabuada))
print("-="*20)