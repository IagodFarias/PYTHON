#faça um menu de operações básicas

num1 = int(input(" digite o primeiro número: "))
num2 = int(input(" digite o segundo número: "))

fim = 1
while fim != 0:
    print(" [1]SOMA \n [2]SUBTRAÇÃO\n [3]MULTIPLICAÇAÕ\n [4]DIVISÃO\n [5]SAIR DO MENU")
    flag = int(input("qual a operação:"))
    if flag == 1:
        resultado = num1 + num2
        print(resultado)
    elif flag == 2:
        resultado = num1 - num2
        print(resultado)
    elif flag == 3:
        resultado = num1 * num2
        print(resultado)
    elif flag == 4:
        if num2 != 0:
           resultado = num1 / num2
           print(resultado)
        else:  print("Não é possível realizar essa operação") 
    elif flag == 5:
        fim = 0
