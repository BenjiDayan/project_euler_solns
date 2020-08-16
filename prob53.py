def fact(n):
    if n == 0:
        return(1)
    return(n*fact(n-1))

def ncr(n, r):
    return(fact(n)/(fact(r)*fact(n-r)))

million = 1000000
n = 0
a = 0
comp = 0

for n in range(100, 0, -1):
    for r in range(a, n):
        if ncr(n,r) > million:
            comp += n-2*r + 1
            a = r-1
            break
    print(n)

print("comp=" + str(comp))
                    
