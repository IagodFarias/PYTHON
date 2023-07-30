# 0,5 - 200km
# 0,45 - viagens mais longas

while True:
    Km = float(input("Digite a distância da viagem: "))

    if Km <= 200:
        VALOR = 0.5 * Km
    else: VALOR = 0.45 * Km
    print(f"O valor da viagem é {VALOR}")