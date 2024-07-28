import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generator():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(4, 6))]
    pass_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_numbers + pass_symbol + pass_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

new_data = {}


def saved():
    web = website_input.get()
    email = Email_input.get()
    pw = password_input.get()

    new_data = {
        web: {
            "email": email,
            "password": pw
        }
    }

    # if web == "" or pw == "":
    if len(web) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops", message="Please don't have any fields empty!")
    else:
        # messagebox.showinfo(title="Title", message="Message")
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email}"
                                                          f"\nPassword: {pw} \nIs it ok to save?")
        if is_ok:
            pyperclip.copy(pw)
            try:
                with open("data_file.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data_file.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data_file.json", "w") as file:
                    json.dump(data, file, indent=4)
                    file.close()
            finally:
                password_input.delete(0, END)
                website_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    user = website_input.get()

    try:
        with open("data_file.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")
    else:
        if user in data:
            messagebox.showinfo(title="Your Data",
                                message=f"Email: {data[user]["email"]}\nPassWord: {data[user]["password"]}")
            pyperclip.copy(data[user]["password"])
        else:
            messagebox.showinfo(title="Oops", message="No Details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=50)

canvas = Canvas(width=200, height=200)
myimg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=myimg)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.config(pady=5)
Email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Label Grid
website_label.grid(column=0, row=1)
Email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=33)
website_input.focus()
Email_input = Entry(width=52)
Email_input.insert(0, "newcustomer2310@gmail.com")
password_input = Entry(width=33)

# Input Grid
website_input.grid(column=1, row=1)
Email_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generator)
generate_button.grid(column=2, row=3)
Add_Button = Button(text="Add", width=44, command=saved)
Add_Button.grid(column=1, row=4, columnspan=2)

Search_button = Button(text="Search Password", command=find_password)
Search_button.grid(column=2, row=1)
window.mainloop()
