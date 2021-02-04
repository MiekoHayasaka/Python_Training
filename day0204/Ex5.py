import random
GAME_COUNT=5
balls=list(range(1,100))
random.shuffle(balls)
awin=bwin=0
for i in range(GAME_COUNT):
	print(f'{i+1}回戦')
	a,b=balls.pop(),balls.pop()
	if a>b:awin+=1;winner='A'
	else:bwin+=1;winner='B'
	print(f'A:{a},B:{b}...{winner}の勝ち')
print('{}対{}で{}の勝ち'.format(max(awin,bwin),min(awin,bwin),'A' if awin > bwin else 'B'))