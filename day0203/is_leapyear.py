def is_leapyear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

#print(is_leapyear(1996))
year = int(input('西暦>>'))

if is_leapyear(year):
    print('西暦{}年は、うるう年です'.format(year))
else:
    print('西暦{}年は、うるう年ではありません'.format(year))
