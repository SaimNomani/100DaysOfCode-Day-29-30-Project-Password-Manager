from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = (website_entry.get()).lower()
    if len(website) == 0:
        messagebox.showinfo(message="please enter the website name")
        return
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            email = data[website]["email"]
            password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(
             message=f"No data file found"
        )
    except KeyError:
        messagebox.showinfo(
            title="No such account", message=f"No account for '{website}' found"
        )

    else:
        messagebox.showinfo(
            title=website, message=f"Email: {email}\nPassword: {password}"
        )


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [
    " ",
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "{",
    "|",
    "}",
    "~",
]


def generate_password():
    password_entry.delete(0, END)
    password = ""
    password_list = [random.choice(letters) for i in range(8)]
    password_list.extend([random.choice(digits) for i in range(6)])
    password_list.extend([random.choice(symbols) for i in range(6)])
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def savePassword():
    new_email = (email_entry.get()).lower()
    new_password = password_entry.get()
    website = (website_entry.get()).lower()
    new_data = {website: {"email": new_email, "password": new_password}}
    print(new_data)
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"entered details:\nemail: {new_email}\npassword: {new_password}\nis it ok to save details?",
    )
    if len(new_email) == 0 or len(new_password) == 0 or len(website) == 0:
        messagebox.showinfo(
            title="oops!!", message="Please don't leave any fields empty"
        )
    elif is_ok:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                messagebox.showinfo(message="Saved successfully.")
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                messagebox.showinfo(message="Saved successfully.")
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
lock_img = PhotoImage(file="logo.png")
lock_canva = Canvas(width=200, height=200)
lock_canva.create_image(100, 100, image=lock_img)
lock_canva.grid(row=0, column=1)

website_label = Label(text="website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=48)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "example@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(
    row=3,
    column=1,
)


search_button = Button(
    text="Search",
    highlightthickness=0,
    width=16,
    command=search_password,
    bg="blue",
    fg="white",
)
search_button.grid(row=1, column=2)
generate_password_button = Button(
    text="Generate Password",
    bg="green",
    fg="white",
    highlightthickness=0,
    width=16,
    command=generate_password,
)
generate_password_button.grid(row=3, column=2, columnspan=1)
add_password_button = Button(
    text="Add",
    width=48,
    bg="red",
    fg="white",
    highlightthickness=0,
    command=savePassword,
)
add_password_button.grid(row=4, column=1, columnspan=2)
window.config(padx=40, pady=40)
window.mainloop()
