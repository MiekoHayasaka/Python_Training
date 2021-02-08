import random

print('ようこそeカードゲームへ')
citizn=4
slave=1
for i in range(5):
    input()
    print(f'{i+1}戦目')
    print(f'手持ちのカード:市民{citizn}枚　奴隷{slave}枚')
    n=int(input('カード選択:「市民」なら「0」、「奴隷」なら「1」を入力>>'))
    print('カードオープン!')
    input()
    pc = random.randrange(5) # 4==皇帝
    if n == 0 and pc != 4:
        print('あなた:市民 PC:市民')
        print('引き分け!')
        citizn -= 1
    elif n == 0 and pc == 4:
        print('あなた:市民 PC:皇帝')
        print('あなたの負け!')
        print('GAME OVER')
        break
    elif n == 1 and pc == 4:
        print('あなた: 奴隷 PC: 皇帝')
        print('あなたの勝ち!')
        print('Congratulation!')
        break
    else:
        print('あなた:奴隷 PC:市民')
        print('あなたの負け!')
        print('GAME OVER')
        break
    print(f'手持ちのカード: 市民{citizn}枚　奴隷:{slave}枚')
