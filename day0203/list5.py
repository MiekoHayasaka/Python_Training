# リスト内包表記

# 1~7の要素を持つリストを作る
x=[n for n in range(1,8)]
print(x)

# 1~7の要素の２乗した値を持つリストを作る
x=[n**2 for n in range(1,8)]
print(x)

# 1~7の要素のうち偶数のリストを作る
x=[n for n in range(1,8) if n % 2 == 0]
print(x)
"""
x=list()
for n in range(1,8):
    if n % 2 == 0:
    x.append(n)
"""

# 入れ子のforでリストを作る
x=[i*10+j for i in range(1,3) for j in range(2,5)]
print(x)
"""
x=list()
for n in range(1,3):
    for j in range(2,5):
        x.append(i*10+j)
"""

# 2次元リストを作る
x=[[i*10+j for j in range(7,10)] for i in range(1,3)]
print(x)

# 単位行列生成
row=col=3
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
print(matrix)

matrix2=[]
for i in range(row):
    temp=[]
    for j in range(col):
        temp.append(1 if i==j else 0)
    matrix2.append(temp)
print(matrix2)
