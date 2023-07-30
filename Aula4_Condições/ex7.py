# verificar se um ano é bissexto ou não

ano = int(input("digite o ano: "))

if ano % 4 == 0 and ano % 100 != 0:
    print("é bissexto")
if ano % 100 == 0 and ano % 400 == 0:
    print("é bissexto")
