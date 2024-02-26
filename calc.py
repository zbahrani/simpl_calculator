from tkinter import Button
import tkinter as tk
import tkinter.messagebox


root =tk.Tk()
root.title('Claculator')
entry=tk.Entry(master=root, borderwidth=3, width=30, bg="blue")
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def botton_click(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y=str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error","Syntax Error")
        
def clear():
    entry.delete(0,tk.END)
    


butten_clear = Button(root, text="clear", borderwidth=20, command=clear)
butten_1 = Button(root, text="1", borderwidth=20, command=lambda: botton_click(1))
butten_2 = Button(root, text="2", borderwidth=20, command=lambda: botton_click(2))
butten_3 = Button(root, text="3", borderwidth=20, command=lambda: botton_click(3))
butten_4 = Button(root, text="4", borderwidth=20, command=lambda: botton_click(4)) 
butten_5 = Button(root, text="5", borderwidth=20, command=lambda: botton_click(5))
butten_6 = Button(root, text="6", borderwidth=20, command=lambda: botton_click(6))
butten_7 = Button(root, text="7", borderwidth=20, command=lambda: botton_click(7))
butten_8 = Button(root, text="8", borderwidth=20, command=lambda: botton_click(8))
butten_9 = Button(root, text="9", borderwidth=20, command=lambda: botton_click(9))
butten_0 = Button(root, text="0", borderwidth=20, command=lambda: botton_click(0))
#operators
butten_Division = Button(root, text="/", borderwidth=20, command=lambda: botton_click("/"))
butten_mines = Button(root, text="-", borderwidth=20, command=lambda: botton_click("-"))
butten_sum = Button(root, text="+", borderwidth=20, command=lambda: botton_click("+"))
butten_multipel = Button(root, text="*", borderwidth=20, command=lambda: botton_click("*"))
butten_equal = Button(root, text="=", borderwidth=20, command=equal)


butten_clear.grid(row=1, column=0)
butten_Division.grid(row=1, column=1)
butten_multipel.grid(row=1, column=2)
butten_sum.grid(row=1, column=3)

butten_1.grid(row=2, column=0)
butten_2.grid(row=2, column=1)
butten_3.grid(row=2, column=2)
butten_mines.grid(row=2, column=3)

butten_4.grid(row=3, column=0)
butten_5.grid(row=3, column=1)
butten_6.grid(row=3, column=2)
butten_equal.grid(row=3, column=3)

butten_7.grid(row=4, column=0)
butten_8.grid(row=4, column=1)
butten_9.grid(row=4, column=2)
butten_0.grid(row=4, column=3)

root.mainloop()





