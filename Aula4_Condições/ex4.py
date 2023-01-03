#desenvolva um programa que leia o comprimente de 3 segmentos de reta e diga se é possível formar um triângulo

r1 = float(input("Digite o segmento de reta: "))
r2 = float(input("Digite o segmento de reta: "))
r3 = float(input("Digite o segmento de reta: "))

if r1 + r2 < r3 and r2 + r3 < r1 and r1 + r3 < r2:
    print("forma um triagulo")
else: 
    print("não vai formar um triagulo")
