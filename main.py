from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
FOREIGN_LANG = "France"
BASE_LANG = "English"
random_word = {}
timeout = ""

# --------------------------------- data -------------------------------------
try:
    dt_frame = read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    dt_frame = read_csv('./data/french_words.csv')

dictionary = dt_frame.to_dict(orient="records")

root = Tk()
root.config(width=900, height=600, padx=50, pady=50, background=BACKGROUND_COLOR)
root.title("Flash Card")

front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(background=BACKGROUND_COLOR)
flashcard = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

txt_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
txt_word = canvas.create_text(400, 263, text="title", font=("Arial", 60, "bold"))


def pick_random_word():
    return random.choice(dictionary)


def flip_card():
    global random_word
    canvas.itemconfig(flashcard, image=back_image)
    canvas.itemconfig(txt_title, text=BASE_LANG, fill="white")
    canvas.itemconfig(txt_word, text=random_word[BASE_LANG], fill="white")
    # root.after_cancel(timeout)


def set_front_face(txt):
    canvas.itemconfig(flashcard, image=front_image)
    canvas.itemconfig(txt_title, text=FOREIGN_LANG, fill="black")
    canvas.itemconfig(txt_word, text=txt, fill="black")


def next_card():
    global random_word, timeout
    root.after_cancel(timeout)
    random_word = pick_random_word()
    set_front_face(random_word["French"])
    timeout = root.after(ms=3000, func=flip_card)


def take_out_card():
    global random_word, dictionary
    dictionary.remove(random_word)
    new_data = DataFrame(dictionary)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


img_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0)
button_wrong.config(relief="flat", background=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(row=1, column=0)

img_right = PhotoImage(file="./images/right.png")
button_right = Button(image=img_right, highlightthickness=0)
button_right.config(relief="flat", background=BACKGROUND_COLOR, command=take_out_card)
button_right.grid(row=1, column=1)

timeout = root.after(ms=3000, func=flip_card)
next_card()

# print(dictionary)

root.mainloop()
