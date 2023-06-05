from tkinter import *
from tkinter import messagebox
import random
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_list = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for i in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password_entry.insert(0, "".join(password_list))

# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search():
    website_name = website_entry.get()
    if website_name == "":
        messagebox.showinfo(title = "Error", message = "You need to enter a website name")
        return
    try:
        with open("100Day Python Bootcamp/Day 29 Password Manager/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "You don't have any password saved")
    else:
        try: 
            record = data[website_name]
        except KeyError:
            messagebox.showinfo(title = "Error", message = f"There is no password asved for {website_name} website")
        else:
            messagebox.showinfo(title = website_name, message = f"Email: {record['email']}\nPassword: {record['password']}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entey.get()
    password = password_entry.get()
    new_line = {
        website:{
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Oops", message = "Please you don't have fileds empty")
    else:
        is_ok = messagebox.askokcancel(title = website, message= f"These are the details entered\nEmail: {email}\nPassword: {password}\n Is this ok to save?")
        if is_ok:
            try:
                with open("100Day Python Bootcamp/Day 29 Password Manager/data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError: data = new_line
            else: 
                data.update(new_line)

            with open("100Day Python Bootcamp/Day 29 Password Manager/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady = 20, bg = "white")

# Create word label
website_label = Label(text = "Website: ", bg = "white")
email_label = Label(text = "Email/Username: ", bg = "white")
password_label = Label(text = "Password: ", bg = "white")

website_label.grid(column=1, row=2)
email_label.grid(column=1, row=3)
password_label.grid(column=1, row=4)

# Create canvas and import logo
canvas = Canvas(width = 200, height = 200, highlightthickness=0, bg = "white")
locker_img = PhotoImage(file = '100Day Python Bootcamp/Day 29 Password Manager/logo.png')
canvas.create_image(100, 100, image = locker_img)
canvas.grid(row = 1, column = 2)

# Create Entry Box
website_entry = Entry(width=21, bg = "white", highlightthickness=0)
email_entey = Entry(width=39, bg = "white", highlightthickness=0)
password_entry = Entry(width=21, bg = "white", highlightthickness=0)

website_entry.grid(column=2, row = 2)
website_entry.focus()
email_entey.grid(column=2, columnspan=2, row = 3)
email_entey.insert(0, "helenbzbz@gmail.com")
password_entry.grid(column=2, row = 4)

# Create Button
search_button = Button(text = "Search", bg = "white", highlightthickness=0, command = search)
add_button = Button(text = "Add", width = 36, bg = "white", highlightthickness=0, command = save)
generate_button = Button(text = "Generate Password", bg = "white", highlightthickness=0, command = password_generator)

search_button.grid(column=3, row = 2)
add_button.grid(column=2, columnspan=2, row = 5)
generate_button.grid(column = 3, row = 4)

window.mainloop()