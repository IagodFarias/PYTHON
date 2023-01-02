#pegar o nome dos 4 aluno, sorteia e devolve um deles.
import random
n1 = str(input("O primeiro aluno é:"))
n2 = str(input("O segundo aluno é:"))
n3 = str(input("O terceiro aluno é:"))
n4 = str(input("O quarto aluno é:"))

lista = [n1, n2, n3, n4]
sorteado = random.choice(lista)

print("\nO sorteado foi {}\n".format(sorteado))