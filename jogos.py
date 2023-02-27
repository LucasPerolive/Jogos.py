#Adiciona os jogos
import forca
import adivinhacao

def escolhe_jogo():
    print("\n*********************************")
    print("***Escolha seu jogo!***")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo você deseja? "))

    #Escolhe entre os dois jogos
    if(jogo == 1):
        print("Jogando forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar_adivinhacao()
    print("*********************************\n")

#Deixa executar direatamente o jogos.py
if(__name__ == "__main__"):
    escolhe_jogo()