import tkinter

# 画面作成
root = tkinter.Tk()
root.geometry('300x200')

# ボタン作成
btn = tkinter.Button(root,text='開始',width=14)
btn.pack(fill='x',padx=20,side='left')
btn2 = tkinter.Button(root,text='終了',width=14)
btn2.pack(fill='x',padx=20,side='left')

root.mainloop()
