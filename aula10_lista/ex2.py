#lista que recebe valores digitados pelo usuário
#verificar qual é o maior e o menor valor da lista

lista = []


for c in range(0, 5):
    lista.append(int(input(print("digite um numero: "))))
    if c == 0:    
        min = max = lista[c]
    else:
        if lista[c] > max:
            max = lista[c]
        elif lista[c] < min:
            min = lista[c]
print(lista)
print(max, min)
    

