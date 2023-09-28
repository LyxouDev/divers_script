from random import choice, randint

alphabets = {}
alphabets[0] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets[1] = "0123456789"

pswd = ''
for _ in range(8):
    jeu_carac = randint(0,len(alphabets)-1)
    carac = choice(alphabets[jeu_carac])
    pswd += carac

print(pswd)
input()