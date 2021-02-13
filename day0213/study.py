import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('English Lesson')
root.geometry('600x400')

cb=ttk.Combobox(root)
cb.bind('<<ComboboxSelected>>')
cb['values']=[1,2,3,4,5,6,7,8,9,10,11,12]
cb.set("チョイス")
cb.pack()

root.mainloop()


