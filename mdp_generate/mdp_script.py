from random import choice, randint

alphabets = {}
alphabets[0] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets[1] = "0123456789"
alphabets[2] = "abcdefghijklmnopqrstuvwxyz"
alphabets[3] = "?@#()[]"

pswd = ''
lg = randint(8,16)
for _ in range(lg):
    jeu_carac = randint(0,len(alphabets)-1)
    carac = choice(alphabets[jeu_carac])
    pswd += carac

print(pswd)
input()