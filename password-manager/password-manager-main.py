from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join([char for char in password_list])
    entryPassword.delete(0, END)
    entryPassword.insert(0, password)
    # pyperclip.copy(password)
# ---------------------------- Search for password in data.json ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as file1:
            data = json.load(file1)
    except:
        print("No Data File Found!")
    else:
        web = entryWeb.get()
        if web in data:
            messagebox.showinfo(title=web, message=f"Email: {data[str(web)]['email']}"
                                                   f"\nPassword: {data[str(web)]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details found for {web}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = entryWeb.get()
    email = entryEmail.get()
    password = entryPassword.get()

    data_dict = {
        web: {
            "email": email,
            "password": password
        }
    }
    if web == "" or password == "":
        messagebox.showwarning(title="oops!", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", "r") as file1:
                old_data = json.load(file1)
        except:
            with open("data.json", "w") as file1:
                json.dump(data_dict, file1, indent=4)
        else:
            old_data.update(data_dict)
            with open("data.json", "w") as file1:
                json.dump(old_data, file1, indent=4)

        # file1.write(f"{web} | {email} | {password}\n")
        entryWeb.delete(0, END)
        entryPassword.delete(0, END)
        entryEmail.delete(0, END)
        entryEmail.insert(0, "nina@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Labels
labelWeb = Label(text="Website:")
labelWeb.grid(column=0, row=1)
labelEmail = Label(text="Email/Username:")
labelEmail.grid(column=0, row=2)
labelPassword = Label(text="Password:")
labelPassword.grid(column=0, row=3)

# Entries
entryWeb = Entry(width=50)
entryWeb.grid(column=1, row=1, columnspan=2)
entryWeb.focus()
entryEmail = Entry(width=50)
entryEmail.grid(column=1, row=2, columnspan=2)
entryEmail.insert(0, "nina@gmail.com")
entryPassword = Entry(width=32)
entryPassword.grid(column=1, row=3, padx=0)

# Buttons
buttonSearch = Button(text="Search", width=14, command=find_password)
buttonSearch.grid(column=2, row=1)
buttonPassword = Button(text="Generate Password", width=14, command=generate_password)
buttonPassword.grid(column=2, row=3)
buttonAdd = Button(text="Add", width=43, command=save)
buttonAdd.grid(column=1, row=4, columnspan=2)

window.mainloop()
