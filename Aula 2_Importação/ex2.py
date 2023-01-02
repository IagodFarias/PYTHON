# faça um programa que leia o valor de Cateto oposto e do Cateto adjacente e devolva o valor da hipotenusa.

from math import hypot
A =  float(input("A:"))
B =  float(input("B:"))
print("o valor da hipotenusa do triangulo abc é {}".format(hypot(A, B)))