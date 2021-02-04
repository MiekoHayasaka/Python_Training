def eat(breakfast,lunch='ラーメン',dinner='カレー'):
    print('朝は{}を食へ゛ました'.format(breakfast))
    print('昼は{}を食へ゛ました'.format(lunch))
    print('晩は{}を食へ゛ました'.format(dinner))

eat('トースト','おにぎり')
print('************************')
eat('バナナ','そば','焼肉')
print('************************')
eat('トースト')
print('************************')
eat('トースト',dinner='焼きそば')

