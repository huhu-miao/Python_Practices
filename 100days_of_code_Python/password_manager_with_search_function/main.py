from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get().title()
    username = user_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if website == "" or password == "" or username == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                   f"Email: {username}\n Password: {password}\n Is it Ok to save?")

        if is_ok:
            try:
                with open("My_passwords.json", 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("My_passwords.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("My_passwords.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                web_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# -------------------------SEARCH PASSWORD---------------------------- #
def search_password():
    website = web_entry.get().title()

    try:
        with open("My_passwords.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")
    else:
        try:
            account = data[website]
        except KeyError:
            messagebox.showwarning(title="Error", message="No details for the website exists")
        else:
            messagebox.showinfo(title=website, message=f"Email: {account['username']}\n"
                                                      f"Password: {account['password']}")
        finally:
            web_entry.delete(0, 'end')
        # The else part could also be handled by using if/else. If you can't easily handle a situation,
        # use try/except, but if you can handle a situation using an if/else statement, use it first.


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Set up the canvas
canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

# Create the labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Set up the entry
web_entry = Entry(width=21)
web_entry.grid(column=1, row=1)
web_entry.focus()

user_entry = Entry(width=38)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "hujingjingjane@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Create the buttons
search_psw_button = Button(text="Search", width=13, command=search_password)
search_psw_button.grid(column=2, row=1)

gen_psw_button = Button(text="Generate Password", command=generate_password)
gen_psw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()