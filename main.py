n = int(input())
array = []
while n > 0:
    array.append(list(map(str, input().split())))
    n-=1
    
def quick(array):
    def sort(arr,l,r):
        if l < r:
            p = part(arr, l, r)
            sort(arr,l,p-1)
            sort(arr,p+1,r)
    def part(arr,l,r):
        pivot = arr[r]
        a = l
        for i in range(l,r):
            if (arr[i] < pivot):
                arr[i], arr[a] = arr[a], arr[i]
                a += 1
        
        arr[r], arr[a] = arr[a], arr[r]
        return a
    
    sort(array, 0, len(array) - 1)
    return array

SDG = {'CleanEnergy':20, 'QualityEducation':16, 'ZeroHunger':12, 'AffordableHousing':8, 'GenderEquity':4}
CSR = {'Excellent':(3/3 * 10), 'Good':(2/3 * 10), 'Fair':(1/3 * 10)}
result = {key: value for key, value in []}
for x in array:
    result[x[0]] = 0

for x in array:
    performance = 0
    performance +=int(x[1]) / pow(10,8) * 40
    for y in SDG:
        if (x[2] == y):
            performance+=SDG[y]
    for y in CSR:
        if (x[3] == y):
            performance+=CSR[y]
    performance+=float(x[4])*2
    performance+=float(x[5])

    result[x[0]] = performance
arr = []
for key,value in sorted(result.items()):
    arr.append(value)
arr = sorted(quick(arr), reverse=True)

for x in arr:
    for y in result:
        if (x == result[y]):
            print(y)
