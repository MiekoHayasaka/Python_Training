import pprint
count=10
x=[[i**2+j for j in range(count)] for i in range(count)]
pprint.pprint(x)
