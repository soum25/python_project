from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_choice = [random.choice(letters) for _ in range(nr_letters)]
    symbols_choice = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_choice = [random.choice(numbers) for _ in range(nr_numbers)]

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    password_list = letters_choice + symbols_choice + numbers_choice
    random.shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.minsize(width=500,height=400)
window.config(padx=70, pady=70)


def save():
    website_value = entry_website.get()
    email_value = entry_email.get()
    password_value = entry_password.get()
    new_data = {
        website_value: {
            "email": email_value,
            "password": password_value
        }
    }

    if len(website_value) == 0 or len(password_value) == 0:
        messagebox.showinfo(title="Empty case", message="Don't let any case empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


def find_password():
    website_value = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="website", message="No details for the website exists ")
    else:
        if website_value in data:
            email = data[website_value]["email"]
            password = data[website_value]["password"]
            messagebox.showinfo(title="website", message=f"Email: {email}\n Password: {password}")


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=5)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 110, image=lock_image)
canvas.grid(column=1, row=0)

entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0,"vafesoumahoro@gmail.com")
entry_password = Entry(width=35)
entry_password.grid(row=3, column=1, columnspan=2 )

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

generate_password_button = Button(text="Generate password", highlightthickness=0, command=password_generator)
generate_password_button .grid(row=3, column=3)
search_button = Button(text="Search", highlightthickness=0, width=12, command=find_password)
search_button .grid(row=1, column=2, columnspan=3)

add_button = Button(text="Add", highlightthickness=0, width=30, command=save)
add_button.grid(row=5, column=1, columnspan=2)


window.mainloop()
