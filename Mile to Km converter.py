from tkinter import *

def mile_to_km():
    miles = input.get()
    km = int(miles)*1.689
    label2.config(text=round(km,2))
screen = Tk()
screen.title("Miles to Km")
screen.minsize(width=300,height=200)
screen.config(padx=55,pady=55)

#Label
label = Label(text="Equals to",font=("Aerial",10))
label.grid(column=0,row=1)
label1 = Label(text="Miles",font=('Aerial',10))
label1.grid(column=2,row=0)
label2 = Label(text="0",font=("Aerial",10))
label2.grid(column=1,row=1)
label3 = Label(text="Km",font=("Aerial",10))
label3.grid(column=2,row=1)

#Entry
input = Entry(width=10)
input.grid(column=1,row=0)

#Button
button = Button(text="Calculate",command=mile_to_km)
button.grid(column=1,row=2)

screen.mainloop()