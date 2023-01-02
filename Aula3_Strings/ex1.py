#crie um programa que leia o nome da pessoa e imprima:
# a) toda maíscula
# b) toda minúscula
# c) conte quantas letras ao todo
# d) quantas letras tem o primeiro nome

nome = str(input("Digite seu nome: ")).strip()
print(nome.upper())
print(nome.lower())
print("A frase possui {} caracteres".format(len(nome) - nome.count(" ")))
frase2 = nome.split()
print("O primeiro nome tem {} caracteres".format(len(frase2[0])))