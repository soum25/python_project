from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = 3000
to_learn = {}
current_card = {}

try:
    data = pd.read_csv("./data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv", encoding="utf-8")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_french_word():
    global flip_timer, current_card, to_learn
    current_card = random.choice(to_learn)
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="french", fill="black")
    canvas.itemconfig(display, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=french_board)
    flip_timer = window.after(timer, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(display, text=current_card["English"])
    canvas.itemconfig(card_image, image=english_board)


def is_known():
    to_learn.remove(current_card)
    word_file = pd.DataFrame(to_learn)
    word_file.to_csv("./data/word_to_learn.csv", index=False)
    next_french_word()


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(timer, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
english_board = PhotoImage(file="./images/card_back.png")

french_board = PhotoImage(file="./images/card_front.png")
card_image = canvas.create_image(400, 280, image=french_board)
card_title = canvas.create_text(400, 150, text="French", font=("Arial", 24, "italic"))
display = canvas.create_text(400, 263, text="", font=("Arial", 30, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)


wrong_mark = PhotoImage(file="./images/wrong.png")
wrong_mark_button = Button(text="Start", font=("Arial", 12, "bold"), image=wrong_mark,
                           highlightthickness=0, borderwidth=0, command=is_known)
wrong_mark_button.grid(row=1, column=0)

correct_mark = PhotoImage(file="./images/right.png")
correct_mark_button = Button(text="Start", font=("Arial", 12, "bold"), image=correct_mark,
                             highlightthickness=0, borderwidth=0, command=is_known)
correct_mark_button.grid(row=1, column=1)

next_french_word()
window.mainloop()
