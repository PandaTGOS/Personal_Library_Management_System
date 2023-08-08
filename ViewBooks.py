from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as S


def SeeBook():
    try:
        getBooks = "select * from books order by Title"
        cur.execute(getBooks)
        dataRow = cur.fetchall()
        y = 0.25
        for i in dataRow:
            tree.insert("",END, values=i)

    except:
        messagebox.showinfo("ERROR", "Unable To Fetch Data")


def View():
    global labelFrame,tree,conn,cur

    conn = S.connect(host="localhost", user="root", password="dpsbn", database="libdb")
    cur = conn.cursor()

    window = Tk()
    window.title("Library")
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    Canvas1 = Canvas(window)
    Canvas1.config(bg="#808080")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(window, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Viewing all the data

    tree = ttk.Treeview(window, column=("c1", "c2", "c3", "c4","c5"), show='headings')
    tree.column("#1", width=45, anchor=CENTER)
    tree.heading("#1", text="ID")

    tree.column("#2", width=100, anchor=CENTER)
    tree.heading("#2", text="TITLE")

    tree.column("#3", width=75, anchor=CENTER)
    tree.heading("#3", text="AUTHOR")

    tree.column("#4", width=50, anchor=CENTER)
    tree.heading("#4", text="PRICE")

    tree.column("#5", width=30, anchor=CENTER)
    tree.heading("#5", text="AVAILABLE")
    tree.place(relx=0.1, rely=0.3, relwidth=0.80, relheight=0.5)

    def EXIT():
        conn.close()
        window.destroy()

    # Making Buttons
    SubmitBtn = Button(window, text="VIEW", bg='#d1ccc0', fg='black', command=SeeBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(window, text="QUIT", bg='#d1ccc0', fg='black', command=EXIT)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    window.mainloop()