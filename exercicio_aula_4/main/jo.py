import matplotlib.pyplot as plt
import numpy as np
ks = np.arange(0.2, 1.1, 0.1)


def f(x, k): 
    return 100 / (1 + k * x)
def g(x):
    return 100 / (1 + 0.1 * x)

x = range(1,10+1)
xs = range(1,35+1)

ys_f = []
ys_g = []
for k in ks:
    for x in xs:
        print(k)
        ys_f.append(f(x, k))
    plt.plot(xs,ys_f)
    ys_f = []

plt.title ('Delay discounting')
plt.xlabel("Delay")
plt.ylabel("Subject Value")
plt.show()