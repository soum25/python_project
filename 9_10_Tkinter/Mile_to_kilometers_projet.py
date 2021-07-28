from tkinter import *

def value_to_convet():
    value = int(input_value.get())
    value_convert = round(value/0.62, 2)
    kilometer_result.config(text=f"{value_convert}")


window = Tk()
window.title("Mile to kilomerters projet")
window.minsize(width=400, height=300)
window.config(padx=60, pady=60)

label_equal = Label(text="is equal to", font=("Arial", 12))
label_equal.grid(column=1, row=2)

kilometer_result = Label(text="0", font=("Arial", 12, "bold"))
kilometer_result.grid(column=3, row=2)

input_value = Entry(width=10)
input_value.grid(column=3, row=1)

calculate = Button(text="Calculate", font=("Arial", 12), command=value_to_convet)
calculate.grid(column=3, row=3)

label_miles = Label(text="Miles", font=("Arial", 12))
label_miles.grid(column=6, row=1)

label_km = Label(text="km", font=("Arial", 12))
label_km.grid(column=6, row=2)



window.mainloop()
