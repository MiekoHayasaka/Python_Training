def sumof(n):
    s=0
    for i in range(1,n+1):
        s += i
    return s

def sumof2(n):
    return sum(range(1,n+1))

def sumof3(n):
    ls=[i for i in range(1,n+1)]
    return (sum(ls))

# 再帰処理
def sumof4(n):
    if n <= 1:
        return n
    else:
        return n+sumof4(n-1)

num=int(input('正の整数>'))
ans=sumof(num)
print(ans)
