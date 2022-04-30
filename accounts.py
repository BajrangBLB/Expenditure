from tkinter import *
import calendar
from datetime import date
import datetime
import sqlite3
from tkinter import font


def createTable():
    try:
        # Creating table nammed expenditure
        c.execute("""CREATE TABLE expenditure (
                    amount integer,
                    purpose text,
                    date text,
                    spender text
                )""")
    except Exception as e:
        pass

def addData(amount, purpose, spender, date):
    # Inserting Data in table
    c.execute(f"""
                INSERT INTO expenditure VALUES (
                    {amount.get()},
                    '{purpose.get()}',
                    '{date}',
                    '{spender.get()}'
                )""")
    conn.commit()
    fetchData()
    calcualte_total()
    # print(amount.get(), "\n", purpose.get(), "\n", spender.get(), "\n", date)

def fetchData():
    dateListBox.delete(1, END)
    spenderListBox.delete(1, END)
    amountListBox.delete(1, END)
    purposeListBox.delete(1, END)

    try:
        # Query the Database
        c.execute("SELECT * FROM expenditure")
        dataQuery = c.fetchall()

        for data in dataQuery:
            # print(data)
            dateListBox.insert(END, data[2])
            spenderListBox.insert(END, data[3])
            purposeListBox.insert(END, data[1])
            amountListBox.insert(END, data[0])
            # dataList.insert(END, str(data[0]) + "\t" + data[1] + "\t" + data[2] + "\t" + data[3])
    
    except Exception as e:
        # dataList.insert(END, "No Data Available")
            dateListBox.insert(END, 'Null')
            spenderListBox.insert(END, 'Null')
            purposeListBox.insert(END, 'Null')
            amountListBox.insert(END, 'Null')
        


def yviewscroll():
    dateListBox.yview()
    purposeListBox.yview()
    spenderListBox.yview()
    amountListBox.yview()

def calcualte_total():
    total_aman = 0
    total_bajrang = 0
    c.execute("SELECT * FROM expenditure WHERE spender == 'Aman'")
    alist= c.fetchall()
    for item in alist:
        total_aman+=item[0]
    
    c.execute("SELECT * FROM expenditure WHERE spender == 'Bajrang'")
    blist = c.fetchall()
    for item in blist:
        total_bajrang+=item[0]

    # print("Aman : ", total_aman, "\nBajrang : ", total_bajrang)
    # print(total_bajrang+total_aman)

    Label(rightbtm,
        text=f"Aman : {total_aman}",
        font=("Arial", 10),
        width=10,
        height=3,).pack(anchor=NW, fill=X)

    Label(rightbtm,
        text=f"Bajrang : {total_bajrang}",
        font=("Arial", 10),
        width=10,
        height=3,).pack(anchor=W, fill=X)

    Label(rightbtm,
        text=f"Total : {total_aman+total_bajrang}",
        font=("Arial", 10),
        width=30,
        height=3,).pack(anchor=SW, fill=X)
    
    Label(rightbtm,
        text=f"Made by Enthusiastic Programmer",
        font=("Arial", 10),
        width=10,
        height=3,).pack(side=BOTTOM, fill=BOTH)

date_today = datetime.datetime.now()
current_date = date_today.day
current_year = date_today.year
current_month = calendar.month_name[date.today().month]
current_month_name = date_today.month
date_string = f"{current_date}-{current_month}-{current_year}"

# Creating Database
# Connecting to the Database
conn = sqlite3.connect(f'{current_month_name}.db')

# Creating cursor
c = conn.cursor()
createTable()

# Creating Main Screen
main_screen = Tk()
main_screen.geometry("1200x700")
main_screen.title('Daily Accounting Software')

leftFrame = Frame(main_screen)
leftFrame.pack(side= LEFT, fill=Y)
scroll_bar = Scrollbar(leftFrame, width=9)

# dataList = Listbox(leftFrame, yscrollcommand= scroll_bar.set, width=100)

dateListBox = Listbox(leftFrame, yscrollcommand=scroll_bar.set, width=15, bg='#f0f0f0', bd=0, fg="#2b2928", font=("Helvetica", 12), highlightthickness=0)
purposeListBox = Listbox(leftFrame, yscrollcommand=scroll_bar.set, width=40, bg='#f0f0f0', bd=0, fg="#2b2928", font=("Helvetica", 12), highlightthickness=0)
spenderListBox = Listbox(leftFrame, yscrollcommand=scroll_bar.set, width=15, bg='#f0f0f0', bd=0, fg="#2b2928", font=("Helvetica", 12), highlightthickness=0)
amountListBox = Listbox(leftFrame, yscrollcommand=scroll_bar.set, width=10, bg='#f0f0f0', bd=0, fg="#2b2928", font=("Helvetica", 12), highlightthickness=0)

scroll_bar.pack( side = RIGHT, fill = Y)
# for line in range(100):
#     dataList.insert(END, 'This is line number' + str(line))
# dataList.pack(side=LEFT, fill=BOTH)

dateListBox.insert(END, 'Date',)
purposeListBox.insert(END, 'Purpose',)
amountListBox.insert(END, 'Amount',)
spenderListBox.insert(END, 'Spender',)

dateListBox.pack(side=LEFT, fill=Y, padx=0, expand=False)
purposeListBox.pack(side=LEFT, fill=Y, padx=0, expand=False)
spenderListBox.pack(side=LEFT, fill=Y, padx=0, expand=False)
amountListBox.pack(side=LEFT, fill=Y, padx=0, expand=False)
scroll_bar.config(command=yviewscroll)
fetchData()

rightFrame=Frame(main_screen, width=20)
rightFrame.pack(fill = X)

labelFrame = Frame(rightFrame)
labelFrame.pack(anchor=N, fill=X)

right_label = Label(labelFrame, 
                    text="Expenditures",
                    font= ("Algerian", 25) )

right_label.pack(side=TOP, fill=X)


# Label(labelFrame,
#         text= date_string,
#         font=("Courier", 20)).pack(anchor=CENTER, fill=X)



gridFrame = Frame(rightFrame)
gridFrame.pack(fill= X)

Label(gridFrame,
        text='Amount',
        font=("Arial", 15),
        width=10,
        height=3,
        ).grid(
            row=1,
            column=2,)

Label(gridFrame,
        text='Purpose',
        font=("Arial", 15),
        width=10,
        height=3,
        ).grid(
            row=2,
            column=2,)

txtAmount = IntVar()
txtPurpose = StringVar()

amount = Entry(gridFrame,
                width=50,
                textvariable=txtAmount,
                ).grid(row=1,
                    column=8,
                    columnspan=5)

purpose = Entry(gridFrame,
                width=50,
                textvariable=txtPurpose,
                ).grid(
                    row=2,
                    column=8,
                    columnspan=5)

txtRadio = StringVar()

Radiobutton(gridFrame,
            text='Aman',
            font=("Arial", 15),
            variable=txtRadio,
            value='Aman',
            ).grid(
                row=4,
                column=2,
                columnspan=6)

Radiobutton(gridFrame,
            text='Bajrang',
            font=("Arial", 15),
            variable=txtRadio,
            height=3,
            value='Bajrang',
            ).grid(
                row=4,
                column=8,
                columnspan=6)


btn = Button(
            gridFrame,
            bg="#00ff00",
            text="Add",
            font=("Courier", 25),
            height=1,
            command=lambda:addData(amount=txtAmount, purpose=txtPurpose, spender=txtRadio, date=date_string),
            ).grid(
                row=12,
                column=5,
                columnspan=5,
            )


# Creating Right Bottom Frame
rightbtm = Frame(rightFrame)
rightbtm.pack(side=BOTTOM, fill=Y)

calcualte_total()
# Commit our Database
conn.commit()
main_screen.mainloop()

# Closing Connection
conn.close()