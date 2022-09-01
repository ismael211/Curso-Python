import random

def carrega_palavra_secreta():
    
    palavras = ['maça','amor','tristeza']

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("\nQual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):

    if(erros == 1):
        print('\nVocê perdeu a cabeça!\n')

    if(erros == 2):
        print('\nVocê o corpo!\n')

    if(erros == 3):
        print('\nVocê perdeu o braço direito!\n')

    if(erros == 4):
        print('\nVocê perdeu o braço esquerdo!\n')

    if(erros == 5):
        print('\nVocê perdeu a perna direita!\n')

    if(erros == 6):
        print('\nVocê perdeu a perna esquerda!\n')


def jogar():

    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)

    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            letras_faltando = str(letras_acertadas.count('_'))
            if (letras_faltando == "0"):
                print(f"PARABÉNS!! Você encontrou todas as letras formando a palavra '{palavra_secreta.upper()}'")
        else:
            erros += 1
            print(letras_acertadas)
            print(f'Ainda faltam acertar {letras_faltando} letras')
            print(f'Você ainda tem {6-erros} tentativas')
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print("Parabéns, você ganhou!")
    else:
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta}")

    print("Fim do jogo")


print("\n*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************\n")

jogar()
