import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# doc for tkinter entries etc: https://tkdocs.com/tutorial/widgets.html#entry


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password=''.join(password_list)
    pw_entry.delete(0, END)
    pw_entry.insert(0, password)
    pyperclip.copy(password)

    #print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website=website_entry.get().title()
    email=email_entry.get()
    pw=pw_entry.get()
    new_data= {
        website: {
            "email": email,
                "password": pw,
        }
    }

    if website=="" or email=="" or pw=="":
        messagebox.showinfo(title="Warning", message="Please fill in all boxes.")
    else:
        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {pw} "
                                                      f" \nIs it OK to save?")


        if is_ok:
            try:
                with open(file="data.json", mode="r") as data_file:
                    json_data = json.load(data_file)
# WRITE into txt>  data.write(f"{website} | {email} | {pw} |\n")
# WRITE TO JASON >>   json.dump(new_data, data, indent=4)
                # reading> dump>
            except FileNotFoundError:
                with open(file="data.json", mode="w") as data_file:
                    json_data={}
                    json.dump(json_data, data_file, indent=4)
            with open(file="data.json", mode="w") as data_file:
                # update> append
                json_data.update(new_data)
                # write > dump
                json.dump(json_data, data_file, indent=4)
            #print(json_data)
            website_entry.delete(0, END)
            pw_entry.delete(0, END)
            website_entry.focus()
# ---------------------------- FIND PW ------------------------------- #
def find_pw():
    website=website_entry.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            json_dict=json.load(data_file)
            #print(json_dict)
    except:
        messagebox.showinfo(title="Information", message="No Data File Found.")
    else:
        keys = []
        for (key, value) in json_dict.items():
            keys.append(key)
        if website in keys:
                email=json_dict[website]["email"]
                pw=json_dict[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {pw}")
        else:
                messagebox.showinfo(title=website, message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title="Password Manager"
window.config(padx=50, pady=50, bg="white")


canvas=Canvas(height=200, width=200, bg="white", highlightthickness=0)
img=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website=Label(text="Website: ", bg="white")
website.grid(column=0, row=1)

email=Label(text="Email/Username: ", bg="white")
email.grid(column=0, row=2)

password=Label(text="Password: ", bg="white")
password.grid(column=0, row=3)

website_entry=Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky=EW)

email_entry=Entry(width=35)
email_entry.insert(0, "minster.lukas@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky=EW)

pw_entry=Entry(width=21)
pw_entry.grid(column=1, row=3, sticky=EW)

add_button=Button(width=36, text="Add", bg="white", highlightthickness=0, borderwidth=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button=Button(text="Search", bg="white", highlightthickness=0, borderwidth=0, command=find_pw)
search_button.grid(column=2, row=1)

generate_bt=Button(text="Generate Password", bg="white",  highlightthickness=0, borderwidth=0, command=gen_pw)
generate_bt.grid(column=2, row=3)

window.mainloop()