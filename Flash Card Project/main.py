from tkinter import *
import pandas as pd
from random import randint

# ---- Constants ---- #
BACKGROUND_COLOR = "#B1DDC6"
DELAY_SECONDS = 3

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Language Setting
language_data_path = "data/french_words.csv"
language = "French"

words_to_learn_path = f"data/{language}_Words_To_Learn.csv"

# ---- Functions ---- #
try:
    data_file = pd.read_csv(words_to_learn_path)
except FileNotFoundError:
    data_file = pd.read_csv(language_data_path)

foreign_words_list = data_file.iloc[:, 0].to_list()
translated_words_list = data_file.iloc[:, 1].to_list()

# word_pairs[randint: pair index][0:French, 1:English]
word_pairs = [(foreign_words_list[i], translated_words_list[i]) for i in range(len(foreign_words_list))]

# lists to identify progress, completed pairs will go from words_to_guess -> words_guessed
words_to_guess = word_pairs
words_guessed = []

foreign_word = str
english_word = str
rand = 0


def learned():
    global foreign_word

    learned_pair = words_to_guess.pop(rand)
    words_guessed.append(learned_pair)

    new_df = pd.DataFrame(words_to_guess, columns=[language, "English"])
    new_df.to_csv(words_to_learn_path, index=False)

    new_word()


def switch_word():
    global english_word

    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(word_displayed, text=english_word, fill="white")
    canvas.itemconfig(language_displayed, text="English", fill="white")


def new_word():
    global english_word, foreign_word, rand
    if len(words_to_guess) > 0:
        rand = randint(0, len(words_to_guess) - 1)
        foreign_word = words_to_guess[rand][0]
        english_word = words_to_guess[rand][1]

        canvas.itemconfig(card_image, image=card_front_img)
        canvas.itemconfig(word_displayed, text=foreign_word, fill="black")
        canvas.itemconfig(language_displayed, text=language, fill="black")
        right_button.config(command=learned)

        window.after(DELAY_SECONDS * 1000, func=switch_word)
    else:
        canvas.itemconfig(card_image, image=card_front_img)
        canvas.itemconfig(word_displayed, text="Cards Completed", fill="black")
        canvas.itemconfig(language_displayed, text="Congrats!", fill="black")
        right_button.config(command=None)
        wrong_button.config(command=None)



# ---- UI ---- #

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_img)
language_displayed = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_displayed = canvas.create_text(400, 263, text="Press any button to start", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button = Button(image=right_img, highlightthickness=0, command=new_word)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_word)
wrong_button.grid(row=1, column=0)

window.mainloop()
