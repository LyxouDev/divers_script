from random import choice, randint
a = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789", "abcdefghijklmnopqrstuvwxyz", "?@#()[]"]
print(''.join(choice(a[randint(0,len(a)-1)]) for _ in range(randint(8,16))))
input()