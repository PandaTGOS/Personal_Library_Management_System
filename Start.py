from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as S
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from SearchBook import *
from LendBook import *

def CreateTable():

    createDB="create database if not exists libdb"
    use="use libdb"
    createTable="create table if not exists books(" \
                "BID int PRIMARY KEY," \
                "Title varchar(200) NOT NULL," \
                "Author varchar(200) NOT NULL, " \
                "Price varchar(15) NOT NULL," \
                "Available varchar(2) NOT NULL )"

    conn = S.connect(host="localhost", user="root", password="dpsbn")
    cur = conn.cursor()

    try:
        cur.execute(createDB)
        cur.execute(use)
        cur.execute(createTable)
        conn.commit()

    except:
        messagebox.showinfo("ERROR","Unable To Create")


def FrontPage():

    window = Tk()
    window.title("Library Management System")
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    # Taking n greater than 0.25 and less than 5
    same = True
    n = 0.23

    # Adding a background image
    background_image = Image.open("libImg.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth * n)
    if same:
        newImageSizeHeight = int(imageSizeHeight * n)
    else:
        newImageSizeHeight = int(imageSizeHeight / n)

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    # Making The Front Page

    Canvas1 = Canvas(window)

    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(window, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="WELCOME TO THE\nLIBRARY MANAGEMENT SYSTEM", bg='black', fg='white',font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # defs for when a button is pressed

    def ADDING():
        window.destroy()
        addBook()
        FrontPage()

    def DELETING():
        window.destroy()
        delete()
        FrontPage()

    def VIEWING():
        window.destroy()
        View()
        FrontPage()

    def SEARCHING():
        window.destroy()
        searchBook()
        FrontPage()

    def LENDING():
        window.destroy()
        LendRetBook()
        FrontPage()


    # Creating Buttons

    btn1 = Button(window, text="ADD A BOOK", bg='black', fg='white', command=ADDING)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(window, text="DELETE A BOOK", bg='black', fg='white', command=DELETING)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn3 = Button(window, text="VIEW BOOK LIST", bg='black', fg='white', command=VIEWING)
    btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    btn4 = Button(window, text="SEARCH A BOOK", bg='black', fg='white', command=SEARCHING)
    btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    btn5 = Button(window, text="LEND/RETURN BOOK", bg='black', fg='white', command=LENDING)
    btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

    window.mainloop()

if __name__=="__main__":
    CreateTable()
    FrontPage()