## f(x) = x+1

# f(1) = 1 + 1
# f(1) = 2

# f(10) = 10 + 1 -> 11

import matplotlib.pyplot as plt
def f(x, n):
    return x**n


lista_xs = range(-50, 50)

# for n in range(20):
lista_ys = []
for x in lista_xs:
    lista_ys.append(f(x, 3))

plt.plot(lista_xs, lista_ys)
plt.title(f"Titulo {3}")


plt.xlabel("X")
plt.ylabel("Y")

plt.show()
lista_ys = []