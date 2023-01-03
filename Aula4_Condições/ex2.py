#leia a velocidade de uma carro. Se ele estiver acima de 70km ele será multado em 7 vezes o valos da diferença

velocidade = int(input("Qual o valor da velocidade agora: "))
if velocidade > 80:
    print("vc está acima da velocidade permitida de 70km/h")
    print("então vc deve pagar uma multa de R${},00 ".format((velocidade - 80)*7))
else:
    print("tenha um bom dia. Dirija com segurança!!!")