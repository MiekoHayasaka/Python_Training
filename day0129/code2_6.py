scores=[88,90,95]
scores.append(34)
scores.append(72)
total=sum(scores)
ave=total / len(scores)
print(f'合計{total}点、平均{ave:.1f}点')
