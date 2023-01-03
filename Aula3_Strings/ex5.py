#leia uma string e diga: i) quantas vezes aparece a letra a, quando foi a primeira e a última vez.

frase = str(input("digite uma frase: ")).strip().upper()
print("a quantidade de vezes que 'A'aparece é {}".format(frase.count("A")))
print("a primeira vez que ela aparece é {} posição".format(frase.find('A')+1)) 
print("a última vez é {} posição ".format(frase.rfind('A')))