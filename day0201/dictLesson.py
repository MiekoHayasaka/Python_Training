dict1=dict() # 空のdict
dict1['apple']='りんご'
dict1['orange']='みかん'
print(dict1)

print(len(dict1)) # 2
dict1['banana']='ばなな'

del dict1['orange']
print(dict1)

print(dict1['apple']) # りんご

# print(dict1['pine']) # error
print(dict1.get('pine')) # None

if 'apple' in dict1:
    print('含まれている')

if 'pine' not in dict1:
    print('含まれていません')

if 'りんご' in dict1.values():
    print('含まれている')
