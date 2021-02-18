import tkinter as tk

def bt_calc():
	pass
def bt_clear():
	pass

mc='#f0edc7'
sc='#51ada8'
s1={'padx':5,'pady':5,'anchor':tk.W}
s2={'padx':10,'pady':5,'anchor':tk.W}
root=tk.Tk();
root.geometry('300x500')
root.title('水割りアルコール度数計算')
root['bg']= mc
tk.Label(fg='white',bg=sc,text='水割りアルコール度数計算').pack(fill=tk.X)
tk.Label(bg=mc,text='お酒の量(ml)').pack(**s1)
e1=tk.Entry(width=10)
e1.pack(**s2)
tk.Label(bg=mc,text='アルコール度数').pack(**s1)
e2=tk.Entry(width=10)
e2.pack(**s2)
tk.Label(bg=mc,text='割る水の量(ml)').pack(**s1)
e3=tk.Entry(width=10)
e3.pack(**s2)
calc_bt=tk.Button(
	text='計算する',
	width=12,
	height=2,
	highlightbackground='#ef8f35',
	#bg='#ef8f35',
	command=bt_calc
)
calc_bt.pack(padx=10,pady=15,anchor=tk.W)
clear_bt=tk.Button(
	text='クリア',
	width=12,
	height=2,
	highlightbackground=sc,
	#bg=sc,
	command=bt_clear
)
clear_bt.pack(padx=10,pady=10,anchor=tk.W)
l1=tk.Label(bg=mc)
l1.place(x=10,y=400)
l2=tk.Label(bg=mc,font=('Arial',24),fg='red')
l2.place(x=125,y=392)
l3=tk.Label(bg=mc)
l3.place(x=180,y=400)
root.mainloop()
