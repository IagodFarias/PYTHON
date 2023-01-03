#leia o nome de uma pessoa e mostre seu primeiro e último nome

nome = str(input("digite seu nome: ")).strip()
nome2 = nome.split()
print("Prazer em te conhecer")
print("Seu primeiro nome é {}".format(nome2[0]))
print("Seu último nome é {}".format(nome2[len(nome2)-1]))
