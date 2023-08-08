from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as S


def deleteBook():
    
    bid = bookInfo1.get()
    deleteSql = "delete from books where BID = '"+bid+"'"

    try:
        cur.execute(deleteSql)
        conn.commit()
        messagebox.showinfo('SUCCESS',"Book Successfully Deleted !")

    except:
        messagebox.showinfo("ERROR","Please Check Book ID")

    bookInfo1.delete(0, END)
    window.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,Canvas1,window,conn,cur

    conn = S.connect(host="localhost", user="root", password="dpsbn", database="libdb")
    cur = conn.cursor()

    window = Tk()
    window.title("Library")
    window.minsize(width=400,height=400)
    window.geometry("600x500")

    
    Canvas1 = Canvas(window)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(window,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(window,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   


    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    def EXIT():
        conn.close()
        window.destroy()

    #Submit Button
    SubmitBtn = Button(window,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(window,text="QUIT",bg='#f7f1e3', fg='black', command=EXIT)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop()