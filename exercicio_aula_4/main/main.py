

idade = 27
nome = "gustavo"

aberto = True # False


ponto = (1,2)

idade = 28
lista_pessoas = [
    {
    'nome': 'garcia',
    'idade': '90',
    'casado': False,

},
    {
    'nome': 'Jonatan',
    'idade': 22,
    'casado': False,

}]
# print(lista_pessoas)
# print(lista_pessoas[0]['idade'])
# print(lista_pessoas[1]['idade'])
soma = 0
for p in lista_pessoas:
    if type(p['idade'])==str:
        soma += int(p['idade'])
    else:
        soma += p['idade']
    
print(soma/len(lista_pessoas))