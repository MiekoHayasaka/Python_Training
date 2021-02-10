import random

input('Enterで対決開始')
while True:
    mydice=[]
    pcdice=[]
    mresult=0
    presult=0
    for i in range(3):
        mydice[i]=random.randint(1,6)
        pcdice[i]=random.randint(1.6)
        mresult += mydice[i]
        presult += pcdice[i]
    print('あなたの出目')
    print(mydice)
    print('コンピューターの出目')
    print(pcdice)
    if mresult < presult:
        print(f'{mresult}対{presult}であなたの負け')
    elif mresult > presult:
        print(f'{mresult}対{presult}であなたの勝ち')
    else:
        print(f'{mresult}対{presult}であいこ')
    yn=input('もう一度対決しますか？<y/n>>>')
    if yn == n:
        print('対決を終了します')
        break


