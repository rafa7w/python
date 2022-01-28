from tkinter import *

window=Tk()

# Para acessar informações sobre os widgets, basta chamar no cmd ipython, fazer a importação do tkinter (from tkinter import *) e rodar, por exemplo, Button?
b1=Button(window, text='Execute')
b1.grid(row=0, column=0)

e1=Entry(window)
e1.grid(row=0, column=1)

t1=Text(window, height=5, width=30)
t1.grid(row=0, column=2)


window.mainloop()
