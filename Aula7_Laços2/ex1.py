#validação de dados
#o usuário deve digita seu sexo [M] ou [F] caso digite outro faça ele repetir

flag = -1
while flag != 0:
    sexo = str(input("digite seu sexo:[M]/[F]\n")).strip().upper()
    if sexo == "M" or sexo == "F":
        flag = 0
    else: flag = -1