from tkinter import *
import turtle

window = Tk()
window.title("this is my first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_click():
    print("I click on the button")
    new_text = input.get()
    my_label.config(text=new_text)

# Label


my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=0)

button = Button(text="Click on me", command=button_click)
button.grid(column=3, row=12)

button2 = Button(text="New button", command=button_click)
button2.grid(column=8,row=0)

input = Entry()
input.grid(column=12, row=12)

window.mainloop()