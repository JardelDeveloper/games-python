import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    #print(numero_secreto)

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range (1, total_tentativas + 1):
        # interpolação de strings (.format)
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_string = input("Digite um número entre 1 e 100: ")
        print("Você digitou o número", chute_string)
        chute = int(chute_string)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            #controle de fluxo (control flow)
            continue

        # melhorando a legibilidade do código
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            # controle de fluxo (control flow)
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))
            # pontos perdidos da rodada
            pontos_perdidos = abs(numero_secreto - chute)
            # subtraindo os pontos perdidos da pontuação total
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()