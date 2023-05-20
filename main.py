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
    
    
# n = int(input())
# arr = []
# while n > 0:
#     arr.append(list(map(str, input().split())))
#     n-=1
    
# Startup1 1507366 Affordable Fair 7.9

i = 1507366
SDG = {'CleanEnergy':20, 'QualityEducation':16, 'ZeroHunger':12, 'AffordableHousing':8, 'GenderEquity':4}
CSR = {'Excellent':9, 'Good':6, 'Fair':3}

for x in arr:
    
