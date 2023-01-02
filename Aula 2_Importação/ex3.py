#programa ler um número e devolve o cos, sin e tg 

from math import cos, sin, tan, radians, trunc
A =  float(input("A:"))
print("O seno de A é {:.2f} \n O cosseno é {:.2f}\n e a tangente é {:.2f}\n".format(cos(radians(A)), sin(radians(A)), tan(radians(A))))