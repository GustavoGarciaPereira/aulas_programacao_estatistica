




palavra = "gustavo"
numero_tentaticas = 6
mostrar = ""
acertos = []
while(numero_tentaticas >= 0):
    letra = input("Digite uma letra")
    if letra in palavra and not(letra in acertos):
        acertos.append(letra)
    else:
        numero_tentaticas -= 1
    
    mostrar = ""
    for letra_palavra in palavra:
        for letra_acertos in acertos:
            if letra_palavra == letra_acertos:
                mostrar += letra_acertos
        else:
            mostrar += '_'

    print(mostrar)
    mostrar = ""
