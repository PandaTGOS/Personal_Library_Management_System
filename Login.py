from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector as S
from Start import *

def checkUser():
    user = Info1.get()
    pswd = Info2.get()

    data=""

    with open("Login.txt","a+") as fh:
        fh.seek(0)
        data=fh.read()

    try:
        if "("+user+","+pswd+")" in data:
            messagebox.showinfo("SUCCESS", "Login Successful")
            window.destroy()
            CreateTable()
            FrontPage()

        else:
            messagebox.showinfo("ERROR", "Login Unsuccessful")
            window.destroy()

    except:
        messagebox.showinfo("ERROR", "Unable To Login")
        window.destroy()


def SignUp():

    user = Info1.get()
    pswd = Info2.get()

    with open("Login.txt","a+") as fh:
        fh.write("\n("+user+","+pswd+")")

    messagebox.showinfo("SUCCESS", "Sign Up Complete !")
    window.destroy()


def LoginFile():
    with open("Login.txt","a+") as fh:
        fh.seek(0)
        data=fh.read()
        if "(admin,admin)" in data:
            x=23
        else:
            fh.seek(0)
            fh.write("(admin,admin)")

def login():
    global Info1, Info2, Canvas1, window, recs

    window = Tk()
    window.title("Library")
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    Canvas1 = Canvas(window)

    Canvas1.config(bg="#3F00FF")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(window, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="L0GIN", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(window, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    lb3 = Label(labelFrame, text="USERNAME : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.40, relheight=0.08)

    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame, text="PASSWORD : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.50, relheight=0.08)

    Info2 = Entry(labelFrame)
    Info2.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)


    def EXIT():
        window.destroy()

    # Submit Button
    SubmitBtn = Button(window, text="SIGN IN", bg='#d1ccc0', fg='black', command=checkUser)
    SubmitBtn.place(relx=0.15, rely=0.87, relwidth=0.18, relheight=0.08)

    SignUpBtn = Button(window, text="SIGN UP", bg='#d1ccc0', fg='black', command=SignUp)
    SignUpBtn.place(relx=0.40, rely=0.87, relwidth=0.18, relheight=0.08)

    quitBtn = Button(window, text="QUIT", bg='#f7f1e3', fg='black', command=EXIT)
    quitBtn.place(relx=0.65, rely=0.87, relwidth=0.18, relheight=0.08)

    window.mainloop()

#__main__
LoginFile()
login()