#sequencia de fibonacci
#  1 1 2 3 5 8 13 21 34 
dig = int(input("Quantos termos da sequencia vc quer: ")) 
t1 = 0
t2 = 1
print("{} -> {} ".format(t1,t2), end = '')
flag = 3
while flag <= dig:
    t3 = t1 + t2
    print("-> {}".format(t3), end='')
    t1 = t2
    t2 = t3
    flag+=1
