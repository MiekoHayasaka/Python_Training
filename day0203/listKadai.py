import pprint
x=[[i*10+j for j in range(1,11)] for i in range(10)]
pprint.pprint(x)

row=col=5
x=[[1 if i==j or i+j==4 else 0 for j in range(col)] for i in range(row)]
pprint.pprint(x)

x=[[]]

