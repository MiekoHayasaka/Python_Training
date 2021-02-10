# 最大公約数を求める
def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y,x%y)

print(gcd(1071,1029)) # 21

