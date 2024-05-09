from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


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
    rand_password = "".join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(0, rand_password)
    pyperclip.copy(rand_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    mail = mail_entry.get()
    password = pass_entry.get()

    new_data = {
        website:
            {"mail": mail,
             "password": password}
    }

    if len(website) * len(mail) * len(password) == 0:
        messagebox.showerror(title="Empty Values Detected", message="Please fill all of the boxes.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Do you want to save these values for {website}?\n"
                                                              f"E-mail/Username: {mail}\nPassword: {password}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except json.decoder.JSONDecodeError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            search_website = website_entry.get()
            credentials = data[search_website]
            messagebox.showinfo(title="Here you go!", message=f"Email: {credentials['mail']}\n"
                                                              f"Password: {credentials['password']}")
    except KeyError:  # this is a common error so it is actually better to use if-else instead of except
        messagebox.showerror(title="Not Found", message="The website you are looking for cannot be found. Please "
                                                        "check spelling.(Case-Sensitive)")
    except FileNotFoundError:
        messagebox.showerror(message="System Error\nData file not found.")


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

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
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

# Search
search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
