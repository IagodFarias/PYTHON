import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def plot_equation_implicit(equation, x_min, x_max, num_points=1000):
    """
    Plota o gráfico de uma equação implícita f(x) = g(x) no intervalo [x_min, x_max].

    Parâmetros:
    - equation: string representando a equação implícita (e.g., '2*x = sin(x) + 10').
    - x_min: limite inferior do intervalo de x.
    - x_max: limite superior do intervalo de x.
    - num_points: número de pontos a serem usados na plotagem (opcional, padrão é 1000).
    """
    # Separar a equação na forma f(x) = g(x)
    lhs, rhs = equation.split('=')
    
    # Definir as funções correspondentes
    f = lambda x: eval(lhs)
    g = lambda x: eval(rhs)
    
    # Gerar os pontos x
    x_vals = np.linspace(x_min, x_max, num_points)
    
    # Calcular os valores de y para f(x) e g(x)
    y_f = f(x_vals)
    y_g = g(x_vals)
    
    # Encontrar as interseções das duas funções
    def h(x): return f(x) - g(x)
    x_intersections = fsolve(h, x_vals)
    y_intersections = f(x_intersections)
    
    # Plotar as funções e suas interseções
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_f, label=f'f(x) = {lhs.strip()}')
    plt.plot(x_vals, y_g, label=f'g(x) = {rhs.strip()}')
    plt.scatter(x_intersections, y_intersections, color='red', zorder=5, label='Interseções')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Gráfico da equação implícita {equation}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de uso:
plot_equation_implicit('2*x = np.sin(x) + 10', -2*np.pi, 2*np.pi)
