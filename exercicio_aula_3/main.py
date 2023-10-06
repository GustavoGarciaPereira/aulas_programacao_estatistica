def f(x):
    return x + 1

def h(x):
    return x + 4

print(f(12))
print(f(14))



print(h(f(14)))



##  IMC = peso / (altura x altura).

# Menor que 18,5	Magreza
# 18,5 a 24,9	Normal
# 25 a 29,9	Sobrepeso
# 30 a 34,9	Obesidade grau I
# 35 a 39,9	Obesidade grau II
# Maior que 40	Obesidade grau III


def imc(peso, altura):
    #return (peso/(altura * altura))
    imc = peso/altura**2
    imc = round(imc, 2)
    return imc

def classifica(valor_imc):
    if valor_imc < 18:
        return "Magreza"
    elif(valor_imc >= 18.5 and valor_imc <= 24.9):
        return "Normal"



print(imc(70, 1.68))
print(classifica(imc(70, 1.68)))
print(classifica(20))