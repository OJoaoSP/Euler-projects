numPrimos = []

for x in range(2, 1000000):
    w = x + 1
    for i in range(2, w):
        if x % i == 0:
            if x == i:
                numPrimos.append(x)
            break
    if len(numPrimos) == 10001:
        print('chego')
        break
		#This is for i know where are
    print(x)

print(numPrimos)
print('fim')
