import random
"""
coin=200
print('残り枚数:',coin)
print('BET枚数を入力。0で終了 1-200>>')
"""
# 3行3列の表を作成し、その表を0-9のランダムの数字で埋める
table=[[random.randint(0,9) for j in range(3)] for i in range(3)]
for row in table:
    print(row)

# 縦と横を入れ替えた表を作成する。(行列の転置)
vertical=[[table[j][i] for j in range(3)] for i in range(3)]
for row in vertical:
    print(row)

# ななめのラインの抽出
cross=[[table[j][j] if i==0 else table[j][2-j] for j in range(3)] for i in range(2)]
for row in cross:
    print(row)
