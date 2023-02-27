#Baixa a biblioteca do random
import random
#Define o jogo como uma função
def jogar_forca():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print (letras_acertadas)

    #Controle de finalização do jogo
    enforcou = False
    acertou = False
    erros = 0

    #Enquanto(True)
    while(not enforcou and not acertou):
        desenha_forca(erros)
        chute = pede_chute()
        """
        Confere as letras e substitui os "_" pela letra acertadas.
        Confere se o chute faz parte da palavra secreta.
        """
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        #Contabiliza os erros, finaliza o jogo caso ganhe ou perca.
        else:
            erros += 1
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print("{}\n".format(letras_acertadas))

    #Mostra o resuntado.
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


#Criando as funções para organizar o código:

"""
Mostra as tentativas e escolher qual letra chutar .
Todas as escolhidas sõa convertidas para maiúsculas e removido os espaçamentos.
"""
def pede_chute():
        chute = input("Letra que você deseja tentar: ")
        chute = chute.strip().upper()
        return chute

#Troca as letras por "_"
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def carrega_palavra_secreta():
    #LER o arquivo de .txt com as palavras
    #LER cada palavra de cada linha, tira os espaçamentos e adiciona da ARRY palavras.
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    #Define a primeira letra para começar a comparar.
    #Cria um laço de repetição onde define a quantidade de letras que compoem a palavra secreta.
    index = 0
    for letra in palavra_secreta:
        #Compara o chute com as letras da palavra secreta.
        #Substitui "_" pela letra.
        #Faz com que passe para próxima letra da palavra.
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1



#Imprime a entrada, a forca e o resultado
def imprime_mensagem_abertura():
    print("\n*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



#Faz com que dê para executar forca.py diretamente e escolher executar ele pelo jogos.py.
if(__name__ == "__main__"):
    jogar_forca()