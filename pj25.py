#pj25

def len_num(num):
    """takes in e.g. 1234, outputs 4"""
    return(len(str(num)))

a = 1
b = 1
comp = [1,1]
count = 3
while True:
    print(count)
    temp = a+b
    comp.append(temp)
    if len_num(temp) == 1000:
        break
    a = b
    b = temp
    count += 1
