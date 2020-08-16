#pj1

threelist = []
fivelist = []
togetherlist = []
sum = 0

for num in range(1000):
    if num % 3 == 0:
        threelist.append(num)
    if num % 5 == 0:
        fivelist.append(num)

togetherlist = threelist
for num in fivelist:
    if not num in togetherlist:
        togetherlist.append(num)

for num in togetherlist:
    sum += num

print(sum)

