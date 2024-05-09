from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    letters_list = [choice(letters) for _ in range(nr_letters)]
    numbers_list = [choice(numbers) for _ in range(nr_numbers)]
    symbols_list = [choice(symbols) for _ in range(nr_symbols)]

    password_list = letters_list + numbers_list + symbols_list
    shuffle(password_list)
    print(password_list)
    rand_password = "".join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(0, rand_password)
    pyperclip.copy(rand_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    mail = mail_entry.get()
    password = pass_entry.get()

    if len(website) * len(mail) * len(password) == 0:
        messagebox.showerror(title="Empty Values Detected", message="Please fill all of the boxes.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Do you want to save these values for {website}?\n"
                                                              f"E-mail/Username: {mail}\nPassword: {password}")
        if is_ok:
            with open("data.txt", "a") as save_data:
                to_write = f"{website} | {mail} | {password}\n"
                save_data.write(to_write)

            website_entry.delete(0, END)
            mail_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# E-Mail
mail_label = Label(text="Email/Username:")
mail_label.grid(row=2, column=0)

mail_entry = Entry(width=35)
mail_entry.insert(0, string="eymenkara@gmail.com")
mail_entry.grid(row=2, column=1, columnspan=2)

# Password
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(row=3, column=2)

# Save
save_button = Button(text="Save", width=36, command=save)
save_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
