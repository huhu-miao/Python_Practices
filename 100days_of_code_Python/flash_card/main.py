from tkinter import *

import pandas
from pandas import *
import random


BACKGROUND_COLOR = "#B1DDC6"

# ----------------------------------DATA SETUP----------------------------------
current_card = {}
to_learn = {}

try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ------------------------------FLASH CARD FUNCTION-----------------------------
def get_next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    get_next_word()
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_card_background, image=card_back_img)


# -----------------------------------UI SETUP-----------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR,
                        borderwidth=0, relief="flat", activebackground=BACKGROUND_COLOR,
                        command=get_next_word)
unknown_button.config(padx=0, pady=0)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR,
                      borderwidth=0, relief="flat", activebackground=BACKGROUND_COLOR,
                      command=is_known)
known_button.config(padx=0, pady=0)
known_button.grid(row=1, column=1)


get_next_word()


window.mainloop()