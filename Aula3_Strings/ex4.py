#leia um nome e diga se possui a string "silva" nele

name = str(input("digite um nome: ")).strip().lower()
print("silva" in name.lower())