from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

#function to define database
def Database():
    global conn, cursor
    #creating student database
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    #creating STUD_REGISTRATION table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ROLLNO TEXT, STU_ADDRESS TEXT)")

#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("900x400")
    #setting title for window
    # display_screen.title("HMS")
    # display_screen.configure(bg='yellow')
    global tree
    global SEARCH
    global name,contact,email,roomno,address
    SEARCH = StringVar()
    name = StringVar()
    contact = StringVar()
    email = StringVar()
    roomno = StringVar()
    address = StringVar()
    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    #first left frame for registration from
    LFrom = Frame(display_screen, width="350")
    LFrom.pack(side=LEFT, fill=Y)
    #seconf left frame for search form
    LeftViewForm = Frame(display_screen, width=500,bg="WHITE")
    LeftViewForm.pack(side=LEFT, fill=Y)
    #mid frame for displaying students record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    #label for heading
    lbl_text = Label(TopViewForm, text="Admin Panel Of Hostel Management System", font=('Calisto MT Bold', 18), width=600,bg="#06518d",fg="white")
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(LFrom, text="Name  ", font=("Calisto MT Bold", 12),fg='#06518d').pack(side=TOP)
    Entry(LFrom,font=("Arial",10,),textvariable=name).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Contact ", font=("Calisto MT Bold", 12),fg='#06518d').pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, ),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Email ", font=("Calisto MT Bold", 12),fg='#06518d').pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, ),textvariable=email).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Room No. ", font=("Calisto MT Bold", 12),fg='#06518d').pack(side=TOP)
    Entry(LFrom, font=("Arial", 10,),textvariable=roomno).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Address ", font=("Calisto MT Bold", 12),fg='#06518d').pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, ),textvariable=address).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="Submit",bg='#06518d',font=("Calisto MT Bold", 10),command=register,fg='white').pack(side=TOP, padx=10,pady=5, fill=X)
    def back():
        display_screen.destroy()

    Button(LFrom, text="Back", bg='#06518d', font=("Calisto MT Bold", 10), command=back, fg='white').pack(
        side=TOP, padx=10, pady=5, fill=X)


    #creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter name to Search", font=("Calisto MT Bold", 12),bg="white")
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=("Calisto MT", 10), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    #creating search button
    btn_search = Button(LeftViewForm, text="Search",bg='#06518d', command=SearchRecord,fg='white',font=("Calisto MT Bold", 12))
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating view button
    btn_view = Button(LeftViewForm, text="View All",bg='#06518d', command=DisplayData,fg='white',font=("Calisto MT Bold", 12))
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating reset button
    btn_reset = Button(LeftViewForm, text="Reset",bg='#06518d', command=Reset,fg='white',font=("Calisto MT Bold", 12))
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating delete buttonzx
    btn_delete = Button(LeftViewForm, text="Delete", bg='#06518d',command=Delete,fg='white',font=("Calisto MT Bold", 12))
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating edit button
    btn_delete = Button(LeftViewForm, text="Edit", bg='#06518d',command=Edit,fg='white',font=("Calisto MT Bold", 12))
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)


   #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Student Id", "Name", "Contact", "Email","Roomno","Address"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('Student Id', text="Student Id", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Roomno', text="Roomno", anchor=W)
    tree.heading('Address', text="Address", anchor=W)
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

#function to insert data into database
def register():
    Database()
    #getting form data
    name1=name.get()
    con1=contact.get()
    email1=email.get()
    room1=roomno.get()
    address1=address.get()
    #applying empty validation
    if name1=='' or con1==''or email1=='' or room1==''or address1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #execute query
        conn.execute('INSERT INTO STUD_REGISTRATION (STU_NAME,STU_CONTACT,STU_EMAIL,STU_ROLLNO,STU_ADDRESS) \
              VALUES (?,?,?,?,?)',(name1,con1,email1,room1,address1));
        conn.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
        #refresh table data
        DisplayData()
        name.set("")
        contact.set("")
        email.set("")
        roomno.set("")
        address.set("")
        conn.close()

def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    name.set("")
    contact.set("")
    email.set("")
    roomno.set("")
    address.set("")

def Delete():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM STUD_REGISTRATION WHERE STU_ID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM STUD_REGISTRATION WHERE STU_NAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

#defining function to access data from SQLite database
def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM STUD_REGISTRATION")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Edit():
    # getting the selected row from the treeview
    selected_row = tree.selection()
    if not selected_row:
        return

    # getting the data from the selected row
    row_data = tree.item(selected_row)['values']
    if not row_data:
        return

    # getting the student ID from the first column of the selected row
    id = row_data[0]

    # getting data for updation
    name1 = name.get()
    contact1 = contact.get()
    email1 = email.get()
    roomno1 = roomno.get()
    address1 = address.get()

    # validating empty fields
    if name1 == '' or contact1 == '' or email1 == '' or roomno1 == '' or address1 == '':
        tkMessageBox.showinfo("Warning", "Please Fill Up All Boxes")
    else:
        # updating the old record
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE STUD_REGISTRATION SET STU_NAME=?, STU_CONTACT=?, STU_EMAIL=?, STU_ADDRESS=? WHERE STU_ID=?",
            (name1, contact1, email1, roomno1, address1))
        conn.commit()
        conn.close()
        DisplayData()
        name.set("")
        contact.set("")
        email.set("")
        roomno.set("")
        address.set("")
        tkMessageBox.showinfo("Message", "Record Updated Successfully")

#calling function
DisplayForm()
if __name__=='__main__':
#Running Application
 mainloop()