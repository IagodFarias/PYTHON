"""
Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. A soma desses múltiplos é 23.

Complete a função solution para que ela retorne a soma de todos os múltiplos de 3 ou 5 abaixo do número passado como parâmetro.

Além disso, se o número for negativo, retorne 0.

Nota: Se o número for múltiplo de ambos 3 e 5, conte-o apenas uma vez.
"""


def solution(number):
    sum = 0
    if number < 0: return 0
    else:
        for c in range(0,number):
            if c % 3 == 0 or c%5 ==0: sum += c

    return sum

