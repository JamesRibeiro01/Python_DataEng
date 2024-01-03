print("*************************************")
print("Bem vindo ao jogo de Advinhação")
print("*************************************")

numero = 100
total_de_tentativas = 3
rodada = 1


while(rodada <= total_de_tentativas):
    print("Tentativa ", rodada, " de ", total_de_tentativas)
    chute = int(input("Digite seu chute"))

    acertou = chute == numero
    maior   = chute > numero
    menor   = chute < numero

    print("Você digitou: ", chute)


    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Seu chute foi maior do que o número secreto")
        elif(menor):
            print("Seu chute foi menor do que o número secreto")

    rodada = rodada + 1

print("Fim de Jogo")
