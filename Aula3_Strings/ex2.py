#leia o nome de uma cidade e diga se ela começa ou não com o nome "santos"

cidade = str(input("digite o nome de uma cidade: ")).lower().strip()
print(cidade.startswith("santos"))