from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return

def clear_button():
    e.delete(0, END)

def add_button():
    global f_num
    global div_pass
    global mult_pass
    first_num = e.get()
    f_num = int(first_num)
    e.delete(0, END)
    mult_pass = False
    div_pass = False

def equal_button():
    second_num = e.get()
    e.delete(0, END)
    if mult_pass == True and div_pass == False:
        e.insert(0, f_num * int(second_num))
    if div_pass == True and mult_pass == False:
        e.insert(0, f_num / int(second_num))
    if div_pass == False and mult_pass == False:
        e.insert(0, f_num + int(second_num))

def mult_button():
    global mult_pass
    global div_pass
    global f_num
    first_num = e.get()
    f_num = int(first_num)
    e.delete(0, END)
    mult_pass = True
    div_pass = False

def div_button():
    global div_pass
    global mult_pass
    global f_num
    first_num = e.get()
    f_num = int(first_num)
    e.delete(0, END)
    div_pass = True
    mult_pass = False



button_1 = Button(root, text = "1", padx = 40, pady= 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady= 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady= 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady= 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady= 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady= 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady= 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady= 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady= 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady= 20, command = lambda: button_click(0))
button_add = Button(root, text = "+", padx = 40, pady= 20, command = lambda: add_button())
button_equal = Button(root, text = "=", padx = 40, pady= 20, command = lambda: equal_button())
button_clear = Button(root, text = "C", padx = 40, pady= 20, command = lambda: clear_button())
button_div = Button(root, text = "/", padx = 40, pady= 20, command = lambda: div_button())
button_mult = Button(root, text = "x", padx = 40, pady= 20, command = lambda: mult_button())
#LOCATIONS OF BUTTONS

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 1)

button_add.grid(row = 4, column = 2)
button_clear.grid(row = 5, column = 1)
button_equal.grid(row = 4, column = 0)
button_div.grid(row = 5, column = 0)
button_mult.grid(row = 5, column = 2)

root.mainloop()
