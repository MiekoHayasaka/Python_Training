def sumof(n):
    if n <= 1:
        return n
    else:
        return n*sumof(n-1)

num=int(input('正の整数>'))
ans=sumof(num)
print(ans)
