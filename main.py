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
    

# Question 2
n = int(input())
arr = []
result = {'Startup1': 0, 'Startup2': 0, 'Startup3': 0, 'Startup4': 0, 'Startup5':0}
while n > 0:
    arr.append(list(map(str, input().split())))
    n-=1
    
# Startup1 1507366 Affordable Fair 7.9

i = 0
SDG = {'CleanEnergy':20, 'QualityEducation':16, 'ZeroHunger':12, 'AffordableHousing':8, 'GenderEquity':4}
CSR = {'Excellent':9, 'Good':6, 'Fair':3}

for x in arr:
    total = 0
    
    total+= int(x[1]) / pow(10,8) * 40
    print('1: ', total)
    for y in SDG:
        if (x[2] == y):
            total+=SDG[y]
    print('2 ', total)
    for y in CSR:
        if (x[3] == y):
            total+=CSR[y]
    print('3: ', total)
    total+=float(x[4])*2
    print('4: ', total)
    total+=float(x[5])
    print("5: ", total)
    
    result[x[0]] = total
    
print(result)

# inputs
# Startup1 7012348 QualityEducation Excellent 7.3 7.9
# Startup2 9393822 GenderEquity Excellent 8.8 9.7
# Startup3 1846780 AffordableHousing Good 6.9 9.2
# Startup4 3961113 ZeroHunger Excellent 9.1 6.5
# Startup5 9081611 ZeroHunger Excellent 5.8 5.8

    
    
