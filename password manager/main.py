from tkinter import  *
from tkinter import messagebox
from random import randint,shuffle ,choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_list():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [choice(letters) for char in range(randint(8, 10))]
    nr_symbols = [choice(symbols) for char in range(randint(2, 4))]
    nr_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list=nr_letters+ nr_symbols+ nr_numbers
    shuffle(password_list)
    password ="".join(password_list)
    password_entry.insert(END,f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web= website_entry.get()
    email=email_entry.get()
    password= password_entry.get()

    if len(web)<1 or len(password) <1:
        messagebox.showinfo(title="ERROR" ,message="Plz fill the details without leaving blank")

    else:
        user_answer = messagebox.askokcancel(title="Website database", message=f"The details u have entered are correct \n"
                                                            f"Website: {web}\n"
                                                            f"Email: {email}\n"
                                                            f"Password: {password}" )
        if user_answer:
            with open("C:/Users/prajwal raj/Desktop/prajwal.txt",mode="a") as file:
                style=f"{web} | {email} | {password} \n"
                file.write(style)
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("PASSWORD GENERATOR")
window.config(padx=50,pady=50)

# LOGO
logo_image=PhotoImage(file="logo.png")
logo=Canvas(width=200,height=200)
logo.create_image(100,100 ,image=logo_image)
logo.grid(row=0,column=1)


# lables
website_lable=Label(text="Website" ,font=("arial",10,"bold"))
website_lable.grid(row=1,column=0)


email_lable=Label(text="Email/Username:" ,font=("arial",10,"bold"))
email_lable.grid(row=2,column=0)

password_lable=Label(text="Password:",font=("arial",10,"bold"))
password_lable.grid(row=3,column=0)


# Entry
website_entry=Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2)


email_entry=Entry(width=35 )
email_entry.grid(column=1,row=2,)
email_entry.insert(END,"prajwal3277@gmail.com")

password_entry=Entry(width=35)
password_entry.grid(row=3,column=1)

# Button
generate_password_button=Button(text="Generate Password",font=("arial",10,"bold") ,command=password_list)
generate_password_button.grid(row=3,column=3)



add_button=Button(text="Add",width=35 ,command=save)
add_button.grid(row=4,column=1,)







window.mainloop()