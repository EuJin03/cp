n = int(input())
array = []
while n > 0:
    array.append(list(map(int, input().split())))
    n-=1

gojo = 0
jogo = 0
for x in array:
    y = len(x) - 1
    while (len(x) % 2 == 0):
        if (x[0] > x[y] or x[y] == x[0]):
            gojo+=x[y]
            jogo+=x[0]
        else:
            gojo+=x[0]
            jogo+=x[y]
        x.pop()
        x.pop(0)
        y-=2
    if (gojo > jogo):
        print("True")
    else:
        print("False")
    gojo = 0
    jogo = 0
