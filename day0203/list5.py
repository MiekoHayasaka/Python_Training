# ���X�g����\�L

# 1~7�̗v�f�������X�g�����
x=[n for n in range(1,8)]
print(x)

# 1~7�̗v�f�̂Q�悵���l�������X�g�����
x=[n**2 for n in range(1,8)]
print(x)

# 1~7�̗v�f�̂��������̃��X�g�����
x=[n for n in range(1,8) if n % 2 == 0]
print(x)
"""
x=list()
for n in range(1,8):
    if n % 2 == 0:
    x.append(n)
"""

# ����q��for�Ń��X�g�����
x=[i*10+j for i in range(1,3) for j in range(2,5)]
print(x)
"""
x=list()
for n in range(1,3):
    for j in range(2,5):
        x.append(i*10+j)
"""

# 2�������X�g�����
x=[[i*10+j for j in range(7,10)] for i in range(1,3)]
print(x)

# �P�ʍs�񐶐�
row=col=3
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
print(matrix)

matrix2=[]
for i in range(row):
    temp=[]
    for j in range(col):
        temp.append(1 if i==j else 0)
    matrix2.append(temp)
print(matrix2)
