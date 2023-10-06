import matplotlib.pyplot as plt

# Dados

# f(x) = x^2
# y = x^2

def f(x):
    return 2**x

xs = range(1,64+1)
ys = []
for x in xs:
    
    print(f"{''.join(list(reversed(str(f(x)))))}:{x}:{f(x)}")
    
    ys.append(f(x))



# Criar o gráfico
plt.plot(xs, ys)

# Adicionar título e rótulos aos eixos
plt.title('Gráfico Simples')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibir o gráfico
plt.show()
