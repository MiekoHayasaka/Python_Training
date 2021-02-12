import tkinter as Tk

root=Tk.Tk()
root.geometry('300x200')
la = Tk.Label(root, text='Hello everybody.',  bg='yellow', relief=Tk.RIDGE, bd=2)
la.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=Tk.W)
lb = Tk.Label(root, text='Oh My God!', bg='red', relief=Tk.RIDGE, bd=2)
lb.grid(row=1, column=0, padx=5, pady=5)
lc = Tk.Label(root, text='See you tomorrow.', bg='LightSkyBlue', relief=Tk.RIDGE, bd=2)
lc.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
