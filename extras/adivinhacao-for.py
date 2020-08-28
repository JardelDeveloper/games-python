import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_tentativas = 3

print(numero_secreto)

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
        print("Parabéns! Você acertou!")
        # controle de fluxo (control flow)
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo")