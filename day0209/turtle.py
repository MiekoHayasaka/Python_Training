import turtle as t
"""
t=turtle.Turtle()
t.shape('turtle')
"""
while True:
    kaku=int(input('カメちゃんに何角形を描いてもらう?(3以上の半角整数,0で終了)>>'))
    if kaku<=0:
        print('bye')
        t.bye()
        break
    elif kaku<=2:
        print('３以上を指定してね')
    else:
        angle = 360/kaku
        for _ in range(kaku):
            t.forward(100)
            t.right(angle)
        t.home()
        turtle.mainloop()
