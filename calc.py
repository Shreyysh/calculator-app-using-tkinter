from tkinter import *
from PIL import Image, ImageTk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    textbox.delete(1.0, "end")
    textbox.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        textbox.delete(1.0, "end")
        textbox.insert(1.0, result)
    except (ValueError, ZeroDivisionError):
        textbox.insert(1.0, "ERROR")

def clear_field():
    global calculation
    textbox.delete(1.0, "end")
    calculation = ""


root = Tk()

root.geometry("360x330")
root.title("Calculator App")
root.config(bg="black")

image = Image.open('icon.jpg')
app_icon: PhotoImage = ImageTk.PhotoImage(image)
root.iconphoto(True, app_icon)

textbox = Text(root,
               height=2, width=64,
               font=("Comic Sans", 24))

textbox.grid(row=0, columnspan=4, sticky='nsew')

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(4, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

btn_1 = Button(root, text="1",
               command=lambda: add_to_calculation(1))
btn_1.grid(row=1, column=0, sticky='nsew')
btn_2 = Button(root, text="2",
               command=lambda: add_to_calculation(2))
btn_2.grid(row=1, column=1, sticky='nsew')
btn_3 = Button(root, text="3",
               command=lambda: add_to_calculation(3))
btn_3.grid(row=1, column=2, sticky='nsew')
btn_4 = Button(root, text="4",
               command=lambda: add_to_calculation(4))
btn_4.grid(row=2, column=0, sticky='nsew')
btn_5 = Button(root, text="5",
               command=lambda: add_to_calculation(5))
btn_5.grid(row=2, column=1, sticky='nsew')
btn_6 = Button(root, text="6",
               command=lambda: add_to_calculation(6))
btn_6.grid(row=2, column=2, sticky='nsew')
btn_7 = Button(root, text="7",
               command=lambda: add_to_calculation(7))
btn_7.grid(row=3, column=0, sticky='nsew')
btn_8 = Button(root, text="8",
               command=lambda: add_to_calculation(8))
btn_8.grid(row=3, column=1, sticky='nsew')
btn_9 = Button(root, text="9",
               command=lambda: add_to_calculation(9))
btn_9.grid(row=3, column=2, sticky='nsew')
btn_0 = Button(root, text="0",
               command=lambda: add_to_calculation(0))
btn_0.grid(row=4, column=0, sticky='nsew')

btn_add = Button(root, text="+",
                 command=lambda: add_to_calculation('+'),
                 width=5)
btn_add.grid(row=4, column=3, sticky='nsew')
btn_minus = Button(root, text="-",
                   command=lambda: add_to_calculation('-'),
                   width=5)
btn_minus.grid(row=3, column=3, sticky='nsew')
btn_multiply = Button(root, text="*",
                      command=lambda: add_to_calculation('*'),
                      width=5)
btn_multiply.grid(row=2, column=3, sticky='nsew')
btn_divide = Button(root, text="/",
                    command=lambda: add_to_calculation('/'),
                    width=5)
btn_divide.grid(row=1, column=3, sticky='nsew')

btn_clear = Button(root, text="AC",
                   command=clear_field)
btn_clear.grid(row=4, column=1, sticky='nsew')

btn_eval = Button(root, text="=",
                  command=evaluate_calculation)
btn_eval.grid(row=4, column=2, sticky='nsew')

root.mainloop()
