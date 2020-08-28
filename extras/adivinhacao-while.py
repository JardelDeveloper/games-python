print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

while (rodada <= total_tentativas):
    #interpolação de strings (.format)
    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute_string = input("Digite o seu número: ")
    print("Você digitou o número", chute_string)
    chute = int(chute_string)

    #melhorando a legibilidade do código
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")