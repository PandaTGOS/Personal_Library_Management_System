from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as S


def BookID():

    Bname=bookInfo1.get()
    Bname.title()

    try:
        getBooks = "select * from books where BID = '" + Bname + "'"
        cur.execute(getBooks)
        dataRow = cur.fetchall()

        if len(dataRow)==0:
            messagebox.showinfo("ERROR", "No Record Found")
        else:
            for i in dataRow:
                Label(window, text="%-30s%-45s%-20s%-5s" % (i[0], i[1], i[2], i[3] + "          "), bg='black',fg='white').place(relx=0.15, rely=0.45)

    except:
        messagebox.showinfo("ERROR","Please Check Book ID")

    bookInfo1.delete(0, END)


def BookTITLE():

    Bname=bookInfo1.get()
    Bname.title()

    try:
        getBooks = "select * from books where Title = '" + Bname + "'"
        cur.execute(getBooks)
        dataRow = cur.fetchall()

        if len(dataRow)==0:
            messagebox.showinfo("ERROR", "No Record Found")
        else:
            for i in dataRow:
                Label(window, text="%-30s%-45s%-20s%-5s" % (i[0], i[1], i[2], i[3] + "          "), bg='black',fg='white').place(relx=0.15, rely=0.45)

    except:
        messagebox.showinfo("ERROR","Please Check Book Title")

    bookInfo1.delete(0, END)


def BookAUTHOR():

    Bname=bookInfo1.get()
    Bname.title()

    try:
        getBooks = "select * from books where Author = '" + Bname + "'"
        cur.execute(getBooks)
        dataRow = cur.fetchall()

        if len(dataRow)==0:
            messagebox.showinfo("ERROR", "No Record Found")
        else:
            for i in dataRow:
                Label(window, text="%-30s%-45s%-20s%-5s" % (i[0], i[1], i[2], i[3] + "          "), bg='black',fg='white').place(relx=0.15, rely=0.45)

    except:
        messagebox.showinfo("ERROR","Please Check Author")

    bookInfo1.delete(0, END)


def searchBook():
    global bookInfo1, bookInfo2, bookInfo3, Canvas1, window, conn, cur

    conn = S.connect(host="localhost", user="root", password="dpsbn", database="libdb")
    cur = conn.cursor()

    window = Tk()
    window.title("Library")
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    Canvas1 = Canvas(window)

    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(window, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Search Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(window, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book title to search
    lb2 = Label(labelFrame, text="Enter Field : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.01)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.01, relwidth=0.62)

    Label(labelFrame, text="%-30s%-50s%-15s%-5s" % ('BID', 'Title', 'Author', 'Price'), bg='black', fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------------", bg='black',fg='white').place(relx=0.05, rely=0.2)


    def EXIT():
        conn.close()
        window.destroy()

    # Submit Button

    Submit1Btn = Button(window, text="BY ID", bg='#d1ccc0', fg='black', command=BookID)
    Submit1Btn.place(relx=0.05, rely=0.87, relwidth=0.18, relheight=0.08)

    Submit2Btn = Button(window, text="BY TITLE", bg='#d1ccc0', fg='black', command=BookTITLE)
    Submit2Btn.place(relx=0.30, rely=0.87, relwidth=0.18, relheight=0.08)

    Submit3Btn = Button(window, text="BY AUTHOR", bg='#d1ccc0', fg='black', command=BookAUTHOR)
    Submit3Btn.place(relx=0.55, rely=0.87, relwidth=0.18, relheight=0.08)

    quitBtn = Button(window, text="QUIT", bg='#d1ccc0', fg='black', command=EXIT)
    quitBtn.place(relx=0.80, rely=0.87, relwidth=0.18, relheight=0.08)

    window.mainloop()