'''
PyScript 1 - 'Number Guess Game'
Author: Jay Bhatt

Desc: In this PyScript i'm using the GUI library - Tkinter
'''

import random
from tkinter import messagebox
from tkinter import *

root = Tk()
root.title("Number Guess Game")
root.geometry('400x300')

number = IntVar()
gusse = IntVar()
gusse.set(7)
count = IntVar()
count.set(0)
a = IntVar()
a.set(random.randint(1, 100))
i = IntVar()
i.set(1)
n = IntVar()
n.set(7)

messagebox.showinfo("Note","Number of guesses is 7  &  Guess Number between 1 to 100")

def checkGuess():
	if(gusse.get() > 0):
		#print("Number of guesses is 7  &  Guess Number between 1 to 100 Number")
		#print(a.get())

		if(int(e1.get()) == a.get()):
			messagebox.showinfo("Result", "Congratulation, YOU ARE WIN THE GAME")
			l4.config(text="Congratulation, YOU ARE WIN THE GAME")
			#count.set(0)
			if(messagebox.askyesno("Continue", "You want to paly again ??")) :
				n.set(7)
				i.set(1)
				a.set(random.randint(1, 100))
				l4.config(text="")
			else :
				exit()

		elif(int(e1.get())<a.get()) :
			# messagebox.showinfo("Result","")		
			l4.config(text="take more gratter number than this")
			count.set(1)

		elif(int(e1.get())>a.get()) :
			l4.config(text="take more smaller number than this")
			count.set(1)

		gusse.set(n.get()-i.get())
		i.set(1+int(i.get()))

	if (count.get()==0 or gusse.get()==0) :
		messagebox.showinfo("Result","YOU ARE LOSS THE GAME")
		s = "YOU ARE LOSS\n Actuall Number is :" + str(a.get())
		l4.config(text=s)
		if(messagebox.askyesno("Continue", "You want to paly again ??")) :
			n.set(7)
			i.set(1)
			a.set(random.randint(1, 100))
			l4.config(text="")
		else :
			exit()

topFrame = Frame(root)
label0 = Label(topFrame, bg='lightgreen', text="Guess Number Game", pady=15, padx=120)

bottomFrame = Frame(root)
l1=Label(bottomFrame, text="Enter Guess Number :", font=("Comic Sans MS", 10, "bold"))
l2=Label(bottomFrame, text="                 ")
l3=Label(bottomFrame, text="Remaining Gusses :", font=("Comic Sans MS", 10, "bold"))

e1=Entry(bottomFrame, bd=3, textvariable=number, font=('calibre',10,'normal'))
e2=Entry(bottomFrame, textvariable=gusse, state=DISABLED)

l4=Label(topFrame,justify=CENTER, font=("Comic Sans MS", 10, "bold"), fg='red')

btn1 = Button(bottomFrame, text="Check", command=checkGuess, bg='white', activebackground='blue', height=2, width= 10)

topFrame.pack()
bottomFrame.pack()

label0.pack(fill=X)
l4.pack()
l1.grid(row=1,column=0, pady= 10)
l2.grid(row=1,column=1, pady= 10)
l3.grid(row=1,column=2, pady= 10)
e1.grid(row=2,column=0)
e2.grid(row=2,column=2)
btn1.grid(row=4,column=1, pady= 30)

root.mainloop()