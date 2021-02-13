import tkinter as tk

def btn_click():
    amount=int(txt_amount.get())
    people=int(txt_people.get())
    dnum = amount / people
    pay = dnum // 100 * 100
    if dnum > pay:
        pay = int(pay+100)
    payorg = amount - pay * (people -1)
    label3['text']='1人あたり{}円({}人)、幹事は{}円です'.format(pay,people-1,payorg)

root=tk.Tk()
root.title('割り勘くん')
canvas=tk.Canvas(root,width=400,height=600,bg='skyblue')
canvas.pack()

label1=tk.Label(root,text='金額',font=('Arial',12),background='skyblue')
label1.place(x=10,y=10)
txt_amount=tk.Entry(root,width=20)
txt_amount.place(x=10,y=40)
lavel2=tk.Label(root,text='人数',font=('Arial',12),background='skyblue')
lavel2.place(x=10,y=80)
txt_people=tk.Entry(root,width=20)
txt_people.place(x=10,y=110)

btn=tk.Button(text='計算する',command=btn_click)
btn.place(x=10,y=160)

label3=tk.Label(root,text='',font=('Arial',12),background='skyblue')
label3.place(x=10,y=200)
root.mainloop() 
