# # # def main():
# # #     # for(int i=0; i<10; i++){
# # #     #     printf();
# # #     # }
# # for numero in [1,2,3,4]:
# #     print(f"{numero}^2 = {numero**2}")
# #     # print(f"bom dia {nome}")
        
# # # main()
# # print("lista ", "g" in "gustavo")
# # ## for

# # ## while
# # lista_numeros = [1,2,3,4,5]
# #                # 0,1,2,3,4
# # cont = 0
# # while(cont < len(lista_numeros)):
# #     # print(cont)
# #     # print(lista_numeros[cont])
    
# #     base = lista_numeros[cont]
# #     conta = base ** 2
    
    
    
# #     print(f"{base} ^ 2 = {conta}")
# #     cont += 1
# #     #print(f"{lista_numeros[cont]}^2 = {lista_numeros[cont]**2}")


# # f(x) = x ^ 2
# # y = x ^ 2
# import matplotlib.pyplot as plt

# def f(x):
#     return x ** 2

# numero = int(input("Numero: "))

# xs = range(1,numero+1)
# ys = []

# for x in xs:
#     ys.append(f(x))


# # print(xs)
# # print(ys)

# plt.plot(xs, ys)


# plt.title('Gráfico Simples')
# plt.xlabel('Eixo x')
# plt.ylabel('Eixo y')

# plt.show()
import matplotlib.pyplot as plt
import math


def f(x) : 
    return (1 - (math.e**(-2*x)))/(2* math.e**-x)
    # return 100 / (1 + 0.5 * x)
    #return math.sinh(x)

xs = range(-10,10)
ys = []

for x in xs:
    ys.append(f(x))
print(xs)
print(ys)

plt.plot(xs,ys)

plt.title ('Delay discounting')
plt.xlabel("Delay")
plt.ylabel("Subject Value")

plt.show()