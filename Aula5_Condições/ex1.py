import random
jogada = str(input(" ")).strip()
cpu = ["pedra", "papel", "tesoura"]
random.shuffle(cpu)
print("cpu: {} \n jogador {} \n".format(cpu[0],jogada))
if jogada in cpu[0]:
    print("empate")
elif jogada == "papel" and cpu[0] == "tesoura":
    print("CPU ganhou")
elif jogada == "tesoura" and cpu[0] == "papel":
    print("Jogador ganhou")
elif jogada == "pedra" and cpu[0] == "tesoura":
    print("Jogador ganhou")
elif jogada == "tesoura" and cpu[0] == "papel":
    print("CPU ganhou")
elif jogada == "pedra" and cpu[0] == "papel":
    print("CPU ganhou")
elif jogada == "papel" and cpu[0] == "pedra":  
    print("Jogador ganhou")
    