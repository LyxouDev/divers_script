from random import choice, randint
a = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789"]
print(''.join(choice(a[randint(0,len(a)-1)]) for _ in range(8)))
input()