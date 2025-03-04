import math
def f(x):
    # Definindo a função f(x) = sin(x) - 2x + 10
    return math.exp(1 / x) - x

def bisseccao(a, b, tolerancia=1e-7, max_iter=100):
    if f(a) * f(b) >= 0:
        print("O método da bissecção falhou. O sinal da função deve ser oposto nas extremidades do intervalo.")
        return None
    
    for i in range(max_iter):
        c = (a + b) / 2  # Ponto médio
        erro = abs(b - a) / 2  # Cálculo do erro
        
        if f(c) == 0 or erro < tolerancia:
            print(f"A raiz encontrada: {c} com erro: {erro}")
            return c  # A raiz foi encontrada
        
        if f(a) * f(c) < 0:
            b = c  # A raiz está no intervalo [a, c]
        else:
            a = c  # A raiz está no intervalo [c, b]
    
    print(f"A raiz aproximada é: {c} com erro: {erro}")
    return c

# Exemplo de uso
a = 1          # Limite inferior do intervalo
b =  2 # Limite superior do intervalo
raiz = bisseccao(a, b)
