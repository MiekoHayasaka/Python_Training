userinfo = input('名前と血液型をカンマで区切って１行で入力>>')
[name,blood] = userinfo.split(',')
blood = blood.upper().strip()
print('{}さんは{}型なので大吉です'.format(name,blood))

print('{:.1f}'.format(2.342)) #2.3

l1=['3','5','6']
print('&'.join(l1))

str='adfgaoegaagagaarigagewoa'
print(str.count('a'))
print(str.replace('a','&'))

for s in 'hello':
    print(s)

for i,s in enumerate('hello',1):
    print('{}文字目は{}です'.format(i,s))

s1='hello'
s2=list(reversed(s1))
print(s2)
print(''.join(s2))

s3=s1[::-1]
print(s3)

print(len(s1))
