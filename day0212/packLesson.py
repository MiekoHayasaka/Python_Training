import tkinter

# 画面作成
root = tkinter.Tk()
root.geometry('300x200')

# ボタン作成
btn = tkinter.Button(root,text='終了')
btn2 = tkinter.Button(root,text='終了')

# 配置
btn.pack(fill='x',padx=30,pady=10,ipady=10)
btn2.pack(fill='x',padx=30,pady=10,ipady=10)

root.mainloop()
