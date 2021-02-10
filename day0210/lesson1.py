num=int(input('正の整数>'))

def tasu(n):
    sums=0
    for i in range(n+1):
        sums += i
    return sums

sums=tasu(num)
print(sums)


