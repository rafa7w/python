# Integrated library
from tkinter import *

window=Tk()

def km_to_miles():
  miles=float(e1_value.get()) * 1.6
  t1.insert(END, miles)

# Para acessar informações sobre os widgets, basta chamar no cmd ipython, fazer a importação do tkinter (from tkinter import *) e rodar, por exemplo, Button?
b1=Button(window, text='Execute', command=km_to_miles)
b1.grid(row=0, column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1=Text(window, height=1, width=30)
t1.grid(row=0, column=2)


window.mainloop()
