from tkinter import *

#creates the main window
root = Tk()
root.title('Calculator')

#creates the entry box where all the inputs and outputs will be visible
SS = Entry(root, width=35, borderwidth=5)
SS.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


#registers the click from the user
def but_click(num):
	SS.insert(END, num)
	return

#clears the main entry box
def but_clear():
	SS.delete(0, END)

#function used for addition
def but_add():
	afirst_num = SS.get()
	global f_numadd
	f_numadd = int(afirst_num)
	SS.delete(0, END)
	global yy
	yy = 1

#function used for subtraction
def but_sub():
	sfirst_num = SS.get()
	global f_numsub
	f_numsub = int(sfirst_num)
	SS.delete(0, END)
	global yy
	yy = 2

#function used for multiplication
def but_mul():
	mfirst_num = SS.get()
	global f_nummul
	f_nummul = int(mfirst_num)
	SS.delete(0, END)
	global yy
	yy = 3

#function used for division
def but_div():
	dfirst_num = SS.get()
	global f_numdiv
	f_numdiv = int(dfirst_num)
	SS.delete(0, END)
	global yy
	yy = 4

#function which displays the output of the arithmetic as given by user
def but_equal():
	second_num = SS.get()
	global s_num
	anss = 0
	s_num = int(second_num)
	SS.delete(0, END)
	if yy == 1:
		anss = f_numadd + s_num
	elif yy == 2:
		anss = f_numsub - s_num
	elif yy == 3:
		anss = f_nummul * s_num
	elif yy == 4:
		anss = f_numdiv / s_num

	SS.insert(0, anss)





#can't pass parameter without lambda[use: lambda: func_name()]

#button creation for GUI of the calculator
but_1 = Button(root, text="1", padx=40, pady=20, command= lambda: but_click(1))
but_2 = Button(root, text="2", padx=40, pady=20, command=lambda: but_click(2))
but_3 = Button(root, text="3", padx=40, pady=20, command=lambda: but_click(3))
but_4 = Button(root, text="4", padx=40, pady=20, command=lambda: but_click(4))
but_5 = Button(root, text="5", padx=40, pady=20, command=lambda: but_click(5))
but_6 = Button(root, text="6", padx=40, pady=20, command=lambda: but_click(6))
but_7 = Button(root, text="7", padx=40, pady=20, command=lambda: but_click(7))
but_8 = Button(root, text="8", padx=40, pady=20, command=lambda: but_click(8))
but_9 = Button(root, text="9", padx=40, pady=20, command=lambda: but_click(9))
but_0 = Button(root, text="0", padx=40, pady=20, command=lambda: but_click(0))

butequal = Button(root, text="=", padx=90, pady=20, command= but_equal)
butadd = Button(root, text="+", padx=39, pady=20, command= but_add)
butsub = Button(root, text="-", padx=39, pady=20, command= but_sub)
butmul = Button(root, text="×", padx=39, pady=20, command= but_mul)
butdiv = Button(root, text="÷", padx=39, pady=20, command= but_div)
butclear = Button(root, text="Clear", padx=79, pady=20, command= but_clear)

#grid method used to place the buttons in their proper place
but_7.grid(row=1, column=0)
but_8.grid(row=1, column=1)
but_9.grid(row=1, column=2)

but_4.grid(row=2, column=0)
but_5.grid(row=2, column=1)
but_6.grid(row=2, column=2)

but_1.grid(row=3, column=0)
but_2.grid(row=3, column=1)
but_3.grid(row=3, column=2)

but_0.grid(row=4, column=0)
butclear.grid(row=4, column=1, columnspan =2)

butequal.grid(row=5, column=1, columnspan =2)
butadd.grid(row=5, column=0)

butsub.grid(row=6, column=0)
butmul.grid(row=6, column=1)
butdiv.grid(row=6, column=2)

#infinite loop used to run the application
root.mainloop()
