# vivo_no_inicio = 30

# dados = [
#     {
#         'Tempo': 1,
#         'N-Censura': 0,
#         'N-Eventos': 1
#     },
#     {
#         'Tempo': 2,
#         'N-Censura': 0,
#         'N-Eventos': 3
#     },
#     {
#         'Tempo': 3,
#         'N-Censura': 0,
#         'N-Eventos': 2
#     },
#     {
#         'Tempo': 4,
#         'N-Censura': 1,
#         'N-Eventos': 1
#     },
#     {
#         'Tempo': 5,
#         'N-Censura': 0,
#         'N-Eventos': 7
#     },
#     {
#         'Tempo': 10,
#         'N-Censura': 2,
#         'N-Eventos': 4
#     },
#     {
#         'Tempo': 20,
#         'N-Censura': 0,
#         'N-Eventos': 2
#     },
#     {
#         'Tempo': 50,
#         'N-Censura': 0,
#         'N-Eventos': 1
#     }
# ]
# lista_x = []
# lista_y = []

# psnfds = dados[0]['N-Eventos']
# for i in dados:
#     lista_x.append(i['Tempo'])
#     morte = i['N-Eventos']/vivo_no_inicio
#     sobrevida = round(100 - (morte*100))
#     psnfds = (sobrevida/100) * psnfds
#     a = 100 * psnfds
#     print(i, vivo_no_inicio, morte, sobrevida, a)
#     lista_y.append(a)
    
#     vivo_no_inicio = vivo_no_inicio - i['N-Eventos'] - i['N-Censura']
    
    
    
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np

# print(lista_x)
# print(lista_y)

# # plt.figure(figsize=(8, 8))
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# plt.grid(True)
# ax.plot(lista_x, lista_y)  # Plot some data on the axes.
# plt.show()


import matplotlib.pyplot as plt

# Dados iniciais
vivo_no_inicio = 30
dados = [
    {'Tempo': 1, 'N-Censura': 0, 'N-Eventos': 1},
    {'Tempo': 2, 'N-Censura': 0, 'N-Eventos': 3},
    {'Tempo': 3, 'N-Censura': 0, 'N-Eventos': 2},
    {'Tempo': 4, 'N-Censura': 1, 'N-Eventos': 1},
    {'Tempo': 5, 'N-Censura': 0, 'N-Eventos': 7},
    {'Tempo': 10, 'N-Censura': 2, 'N-Eventos': 4},
    {'Tempo': 20, 'N-Censura': 0, 'N-Eventos': 2},
    {'Tempo': 50, 'N-Censura': 0, 'N-Eventos': 1}
]

# Cálculo da sobrevida cumulativa
lista_x, lista_y = [], []
psnfds = 1  # Inicializando com 100% de sobrevida

for i in dados:
    lista_x.append(i['Tempo'])

    morte = i['N-Eventos'] / vivo_no_inicio
    psnfds *= (1 - morte)

    lista_y.append(100 * psnfds)
    vivo_no_inicio -= (i['N-Eventos'] + i['N-Censura'])

# Plotar os resultados
fig, ax = plt.subplots()
plt.grid(True)
ax.plot(lista_x, lista_y, drawstyle='steps-post', marker='o')
ax.set_title("Sobrevida Kaplan-Meier")
ax.set_xlabel("Tempo")
ax.set_ylabel("Probabilidade de Sobrevida (%)")
plt.show()
