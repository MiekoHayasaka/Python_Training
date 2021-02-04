dist=384400*1000*1000 # 月までの距離(mm)
thickness=1 # 紙の厚さ(mm)
count=0 # 折り曲げた回数

while thickness < dist:
    thickness *= 2 # 厚みを2倍にする
    count += 1
    print(count,'回折り曲げた','厚み：',thickness)
print(count,'回で月に到達しました。')
