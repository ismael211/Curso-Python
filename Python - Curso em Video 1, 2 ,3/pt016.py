from playsound import playsound

while True:
    b=str(input("Digite B para parar e P para tocar: ")).strip().upper()[0]
    if b == 'B':
        break
    if b == 'P':
        playsound('nico.mp3')    