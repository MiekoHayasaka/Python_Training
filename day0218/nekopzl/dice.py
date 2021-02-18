import random
input('Enterで対決開始')
while True:
	print('あなたの出目')
	you=[random.randint(1,6) for i in range(3)]
	print(you)
	print('コンピュータの出目')
	pc=[random.randint(1,6) for i in range(3)]
	print(pc)
	you_sum=sum(you)
	if len(set(you)) == 1:
		you_sum*=2
	pc_sum=sum(pc)
	if len(set(pc))==1:
		pc_sum *=2
	result='あいこ' if you_sum == pc_sum else 'あなたの勝ち' if you_sum > pc_sum else 'あなたの負け'
	print(f'{you_sum}対{pc_sum}で{result}')
	select=input('もう一度対決しますか？<y/n>>>')
	if select != 'y':
		break
print('対決を終了します')
