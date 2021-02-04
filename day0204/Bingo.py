import random

COINS=200
TW=3
table=[]

def createTable():
    global table
    # 3行3列の表を作成し、その表を0-9のランダムの数字で埋める
    #table=[[random.randint(0,9) for j in range(3)] for i in range(3)]
    table=[[random.randint(0,9) for j in range(TW)] for i in range(TW)]
    for row in table:
        print(row)

#createTable()

def countBingoLine():
    global table
    # 縦と横を入れ替えた表を作成する。(行列の転置)
    vertical=[[table[j][i] for j in range(TW)] for i in range(TW)]
    # ななめのラインの抽出
    cross=[[table[j][j] if i==0 else table[j][TW-1-j] for j in range(TW)] for i in range(2)]
    bingo_line=0
    for row in table+vertical+cross:
        if len(set(row))==1:
            bingo_line+=1
    return bingo_line

#print(countBingoLine())
    
while True:
    print(f'残り枚数:{COINS}')
    bet=int(input(f'BET枚数を入力。0で終了　1-{COINS}>>'))
    if bet==0:
        break
    if bet > COINS:
        print('コインが不足しています')
        continue

    COINS -= bet
    createTable()
    bingo_line=countBingoLine()
    if bingo_line > 0:
        get_coin=bingo_line*12*bet
        COINS+=get_coin
        print(f'{bingo_line} LINE BINGO!win:{get_coin}')
    else:
        print('boo')

    if COINS==0:
        print('コインがなくなりました')
        break
print('Game Over')



