#Baixa a biblioteca do random / cria função do jogo.
import random
def jogar_adivinhacao():
    #Parte estética do jogo.
    print("\n*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    #Variáveis do jogo / Função que gera uma número aleatorio entre 1 e 100.
    numero_secreto = round(random.randrange(1,101))
    tentativas = 0
    pontos = 1000

    #Define quantidade de tentativas
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Define o nível:"))
    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    #Laço de repetição.
    for rodada in range(1, tentativas + 1):

    #Semelhate a como é funciona o printf da linguagem C, no python precisa da função .format.
        print("Tentativa {} de {}".format(rodada, tentativas))
    #Escolher o numero para chutar, e converter ele de str para int.
        chute = int(input("\nDigite um número entre 1 e 100: "))
        print("Você digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
    #Comparação entre o chute e número secreto
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

    #Condicional para ver se o numero é igual ou diferente.
        if (acertou): 
            print("\nVocê ACERTOU e fez {} pontos!!!".format(pontos))
            break
        else:
            if(maior):
                print("\nVocê ERROU! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("\nVocê ERROU! O seu chute foi menor do que o número secreto.")
    #Faz a contagem de pontos.    
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("*********************************\n")
    print("O valor secreto era: {}".format(numero_secreto))
    print("*********************************\n")
print("FIM DO JOGO!!!")

#Faz com que dê para executar adivinhacao.py diretamente e escolher executar ele pelo jogos.py.
if(__name__ == "__main__"):
    jogar_adivinhacao()