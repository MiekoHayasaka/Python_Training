import random

data=list()
data_count=100
for _ in range(data_count):
    data.append(random.randint(1,100))
print(data)
for i in range(data_count):
    if data[i]==77:
        print('77->',i)
        break
else:
    print('77->なし')
"""
# コレクションを回しながら、カウンタ変数も使いたい場合
for i,num in enumerate(data):
    if num == 77:
        print('77->',i)
        break
else:
    print('77->なし')
"""