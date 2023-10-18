import matplotlib.pyplot as plt
def f(x): 
    return 100 / (1 + 0.5 * x)

def g(z):
    return 100 / (1 + 0.1 * z)

x = range(1,10+1)
z = range(1,10+1)

xs = range(1,35+1)
zs = range(1,35+1)
ys = []
zys = []

for x in xs:
    ys.append(f(x))

for z in zs:
    zys.append(g(z))

print(xs)
print(ys)

plt.plot(xs,ys)
plt.plot(zs,zys)

plt.title ('Delay discounting')
plt.xlabel("Delay")
plt.ylabel("Subject Value")
plt.show()