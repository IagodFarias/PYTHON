#detector de palídromos
#palídromo: diz-se de ou frase ou palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa.

frase = str(input("digite uma frase: ")).strip().lower()
flag = 0  # a frase não é um palíndromo por default
cont = len(frase)
for c in range(0 , cont):
    for d in range(cont-1, -1, -1):
        if frase[c] == frase[d]:
            flag = -1
        else: flag = 0
if flag == -1:        
    print("A frase é um palídromo")
else: print("A frase não é um palídromo")