#Program made by Group 9 of INF221
#Abgao, Deguito, Dela Viña

#This program is called "Age Calculator". It functions to calculate the age of the user, given that they have provided their birthdate.

import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import messagebox
from datetime import date

while True:
    
    #GUI
    root = tk.Tk()

    #Window of the Program
    canvas1 = tk.Canvas(root, width=800,height=600)
    canvas1.pack()
    root.resizable(False,False)
    root.title("AGE CALCULATOR by Group 9")
    root.iconbitmap("NU_Seal.ico")

    #Widgets

    #Logo
    photo = PhotoImage(file="Age_Calculator2.png")
    myimage = Label(image=photo).place(x=275,y=0)
    
    photo1 = PhotoImage(file="NU_Seal1.png")
    myimage = Label(root, image=photo1,).place(x=700, y=20)

    #Function to Redirect to NU Website
    def callback(event):
        webbrowser.open_new(event.widget.cget("text"))
        
    lbl = tk.Label(root, text=r"https://national-u.edu.ph/", fg="blue", cursor="hand2", font=40)
    lbl.pack()
    lbl.bind("<Button-1>", callback)
    
    #Function to calculate the age
    def CalculateAge():
        
        #Gets the present Month, Day, and Year
        today=date.today()
        currentDay=today.day
        currentMonth=today.month
        currentYear=today.year
        
        #Gathers the data input by the user
        birthDate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
        
        #Formula in calculating the age
        if birthDate.day > currentDay and birthDate.month > currentMonth:
            dayAge1= (currentDay+30)-birthDate.day + 1
            monthAge1= ((currentMonth-1)+12) - birthDate.month
            yearAge1= (currentYear-1) - birthDate.year
            print(Label(text=f"You are {yearAge1} years {monthAge1} months and {dayAge1} days old", font=30).place(x=275,y=500))
            
        elif birthDate.day < currentDay and birthDate.month < currentMonth:
            dayAge1= currentDay-birthDate.day
            monthAge1= currentMonth - birthDate.month 
            yearAge1= currentYear - birthDate.year
            print(Label(text=f"You are {yearAge1} years {monthAge1} months and {dayAge1} days old", font=30).place(x=275,y=500))
                
        elif birthDate.day > currentDay and birthDate.month < currentMonth:
            dayAge1= (currentDay+31)-birthDate.day
            monthAge1= currentMonth - birthDate.month - 1
            yearAge1= currentYear - birthDate.year
            print(Label(text=f"You are {yearAge1} years {monthAge1} months and {dayAge1} days old", font=30).place(x=275,y=500))
        
        elif birthDate.day < currentDay and birthDate.month > currentMonth:
            dayAge1= currentDay - birthDate.day
            monthAge1= (currentMonth + 12) - birthDate.month
            yearAge1= (currentYear - 1) - birthDate.year
            print(Label(text=f"You are {yearAge1} years {monthAge1} months and {dayAge1} days old", font=30).place(x=275,y=500))
            
        elif birthDate.day > currentDay and birthDate.month == currentMonth:
            dayAge1= (currentDay+31)-birthDate.day
            monthAge1= currentMonth
            yearAge1= (currentYear - 1) - birthDate.year
            print(Label(text=f"You are {yearAge1} years {monthAge1} months and {dayAge1} days old", font=30).place(x=275,y=500))
            
        elif birthDate.day < currentDay and birthDate.month == currentMonth:
            dayAge1= currentDay - birthDate.day
            monthAge1= (currentMonth*2) - birthDate.month
            yearAge1= (currentYear - 1) - birthDate.year
            print(Label(text=f"You are {yearAge1} years {monthAge1} months and {dayAge1} days old", font=30).place(x=275,y=500))
            
        else:
            dayAge1= currentDay - birthDate.day
            monthAge1= currentMonth - birthDate.month
            yearAge1= currentYear - birthDate.year
            print(Label(text=f"You are {yearAge1} years {monthAge1} months and {dayAge1} days old", font=30).place(x=275,y=500))

    #Text label of Month, Day, and Year on the UI
    Label(text="Month", font=23).place(x=200, y=250)
    Label(text="Day", font=23).place(x=200, y=300)
    Label(text="Year", font=23).place(x=200, y=350)

    #Requires the entry to the Month, Day, and Year's to only be int type
    monthValue = IntVar()
    dayValue = IntVar()
    yearValue = IntVar()

    #Text for Month, Day, and Year Label
    monthEntry = Entry(root,textvariable=monthValue, width=22,bd=3,font=20)
    monthEntry.place(x=300,y=250)

    dayEntry = Entry(root,textvariable=dayValue, width=22,bd=3,font=20)
    dayEntry.place(x=300,y=300)

    yearEntry = Entry(root,textvariable=yearValue, width=22,bd=3,font=20)
    yearEntry.place(x=300,y=350)

    #A function where a message will pop-up when the calculate button is pressed, and will then ask whether to convert again or not (program closes if the answer is no)
    def onClick():
        
        calculate_again = tk.messagebox.askquestion('Age Calculator by Group 9', 'Do you want to convert again?', icon='question')
        if calculate_again == 'yes':
            tk.messagebox.showinfo('Age Calculator by Group 9', 'You will now return to the age calculator screen')
        else:
            root.destroy()

    #Calculate Button
    Calculate_Button = Button(text="CALCULATE YOUR AGE",font=("Helvetica", 18),bg="#2c3d8d",fg="#eccd27",width=20,height=2,command=lambda:[CalculateAge(),onClick()]).place(x=255,y=400)


    root.mainloop()
    
    break