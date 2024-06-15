import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.config(width=900, height=600, padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Flash Card")

card_image = tk.PhotoImage(file="./images/card_front.png")
canvas = tk.Canvas(width=800, height=526, highlightthickness=0)
canvas.config(background=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_image)
canvas.grid(row=0, column=0, columnspan=2)

txt_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
txt_word = canvas.create_text(400, 263, text="title", font=("Arial", 60, "bold"))

img_wrong = tk.PhotoImage(file="./images/wrong.png")
button_wrong = tk.Button(image=img_wrong, highlightthickness=0)
button_wrong.config(relief="flat", background=BACKGROUND_COLOR)
button_wrong.grid(row=1, column=0)

img_right = tk.PhotoImage(file="./images/right.png")
button_right = tk.Button(image=img_right, highlightthickness=0)
button_right.config(relief="flat", background=BACKGROUND_COLOR)
button_right.grid(row=1, column=1)

window.mainloop()
