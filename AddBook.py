from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as S


def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    price = bookInfo4.get()
    av= bookInfo5.get()

    title=title.title()
    author=author.title()
    
    insertBooks = "insert into books values('"+bid+"','"+title+"','"+author+"',"+price+",'"+av.upper()+"')"

    try:
        cur.execute(insertBooks)
        conn.commit()

        messagebox.showinfo('SUCCESS',"Book Added Successfully")
    except:
        messagebox.showinfo("ERROR","Unable To Add Book")

    window.destroy()

    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,Canvas1,window,conn,cur

    conn = S.connect(host="localhost", user="root", password="dpsbn", database="libdb")
    cur = conn.cursor()

    window = Tk()
    window.title("Library")
    window.minsize(width=400,height=400)
    window.geometry("600x500")


    Canvas1 = Canvas(window)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(window,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="ADD BOOKS", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(window,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="BOOK ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="TITLE : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="AUTHOR : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    #Book Price
    lb4 = Label(labelFrame, text="PRICE : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Book Availability
    lb5 = Label(labelFrame, text="AVAILABLE(Y/N) : ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.80, relheight=0.08)

    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3, rely=0.80, relwidth=0.62, relheight=0.08)

    def EXIT():
        conn.close()
        window.destroy()

    #Submit Button
    SubmitBtn = Button(window,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(window,text="QUIT",bg='#f7f1e3', fg='black', command=EXIT)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop()