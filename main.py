#alvin ocasio jr
# 2/6/2024

message = "thisisatest"
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for x in range(len(LETTERS)):
    encoded = ''
    for y in message:
        if y in LETTERS:
           n = LETTERS.find(y)
           n = n - x
           if n < 0:
               n = n + len(LETTERS)
           encoded = encoded + LETTERS(n)
        else:
            encoded = encoded + y
    print(" shift key ", x ": ",  encoded)




