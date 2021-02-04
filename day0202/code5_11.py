def calc_average(scores):
    avg = sum(scores) / len(scores)
    print('平均点は{}です'.format(avg))

calc_average([10,20,30])
calc_average((10,20,30))
calc_average({20,20,30,10,40})
calc_average(range(100))

def plus(x,y):
    answer=x+y
    return answer

ans=plus(100,200)
print(ans)
