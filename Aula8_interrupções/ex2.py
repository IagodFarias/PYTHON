
flag = 0
while flag != 999:
    base = int(input())
    if base >= 0:
        for c in range(0,10):
            print(f'{base * c}')
    else: break

