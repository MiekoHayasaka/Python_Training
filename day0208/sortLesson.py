import random

l1=[1,5,3,9]
l1.sort() # 自身を変更
print(l1) 
random.shuffle(l1) # 破壊的な関数
print(l1)

l2=sorted(l1) # 新たに作成
print(l2)
print(l1)
