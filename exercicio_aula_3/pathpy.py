# import pandas as pd
# import pyreadstat
# df, meta = pyreadstat.read_sav('PATH_Aula.sav')


# # df_processed = df.some_processing_method()
# import pathpy as pp
# network = pp.Network.from_pandas(df)



import sympy as sp
import matplotlib.pyplot as plt

def main():
    # Definir a variável
    x = sp.symbols('x')

    # Definir a função
    # f = 'x**2 + 2*x + 1'
    f = input('Equação: ')

    # Calcular a derivada
    f_prime = sp.diff(f, x)

    # Exibir a derivada
    print(f_prime)
    xs = range(-100, 100)
    ys = []

    ys = list(map(lambda i: f_prime.subs(x, i).evalf(), xs))
    # for i in xs:
    #     f_prime_at_3 = 

    #     # value_at_3 = f_prime_at_3
    #     ys.append(f_prime_at_3)
    #     # print(value_at_3)

    plt.plot(xs, ys)
    

    plt.title(f_prime)
    plt.xlabel("Delay")
    plt.ylabel("Subject Value")

    plt.show()
    

def cauculo(funcao):
    x = sp.symbols('x')

    # Definir a função
    # f = 'x**2 + 2*x + 1'

    # Calcular a derivada
    f_prime = sp.diff(funcao, x)

    # Exibir a derivada
    # print(f_prime)
    return f_prime


def desenhar_grafico(f_prime):
    x = sp.symbols('x')
    xs = range(100)
    ys = []
    for i in xs:
        f_prime_at_3 = f_prime.subs(x, i)

        value_at_3 = f_prime_at_3.evalf()
        ys.append(value_at_3)
        # print(value_at_3)
    
    plt.plot(xs,ys)

    plt.title (f_prime)
    plt.xlabel("Delay")
    plt.ylabel("Subject Value")

    plt.show()
if __name__ == '__main__':
    main()