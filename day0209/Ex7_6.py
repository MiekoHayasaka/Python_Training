from random import randint as ri

print('数あてゲームを始めます。３桁の数を当ててください!')
answer=list()
for i in range(3):
    answer.append(ri(0,9))
print(answer)

while True:
    hit=0
    boll=0
    prediction=list()
    for i in range(3):
        prediction.append(int(input(f'{i+1}桁目の予想を入力>>')))

    for i in range(3):
        if answer[i] == prediction[i]:
            hit += 1
        else:
            for j in range(3):
                if answer[i] == prediction[j] and i != j:
                    boll += 1
    print(f'{hit}ヒット！{boll}ボール！')
    if hit == 3:
        print('正解です！')
        break
    else:
        yn=int(input('続けますか？1:続ける 2:終了'))
        if yn == 2:
            print(f'正解は{answer}でした')
            break
