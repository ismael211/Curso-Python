# from random import choice

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


word = str(input('Digita a palavra: ')).lower()

palavra = word

print("JOGO DA FORCA 1.0\n")
print("Bem vindo ao JOGO DA FORCA. Boa sorte!\n")

chances = 6
alfabeto = list("abdcefghijklmnopqrstuvwxyz")
tentativas = []
erros = 0

while True:
    
    print(tentativas)
    print("Chances: ",chances)

    for letra in palavra:
        if letra in tentativas:
            print(letra, end = ' ')
        else:
            print('_', end= ' ')

    print('\n\nDigite "SAIR" para sair do programa!')
    palpite = input("Digite seu palpite: ").lower()

    if palpite == "sair":
        print('Obrigado por jogar, até mais!')
        break
            
    elif palpite not in alfabeto or palpite == '':
        print("Por favor digite uma letra!")
        continue
            
    elif palpite in tentativas:
        print("\nVocê já tentou essa letra. Tente outra!\n")
        continue

    tentativas.append(palpite)

    if palpite in palavra:
        print("ACERTOU!")
        
    else:
        erros +=1
        desenha_forca(erros)
        chances -=1

    if chances == 0:
        print("Você Perdeu! Game over!")
        break

    elif set(palavra).issubset(set(tentativas)):
        print("Parabéns, você acertou!")
        break
        

print('fim de jogo')