#pj2

def get_fibonacci(num):
    a = [1,2]
    while a[-1] < num:
        a.append(a[-2] + a[-1])
    return(a)

fibs = get_fibonacci(4000000)
ev_list = []
sum = 0

for num in fibs:
    if num % 2 == 0:
        ev_list.append(num)
sum = 0
for num in ev_list:
    sum += num
print(sum)
