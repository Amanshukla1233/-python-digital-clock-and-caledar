from tkinter import *
from tkcalendar import Calendar
import time
# caleder function
def get_date():
    date.configure(text="Selected Date is  " +today.get_date())

root=Tk()
root.title("Digital clock")
root.geometry('950x650')
root.config(bg="blue")

# digital clock function
def mytime():
    mytext=time.strftime("%I:%M:%S  %p")
    mytext2=time.strftime("%A")
    Mylabel.config(text=mytext)
    mylabel2.config(text=mytext2)
    Mylabel.after(100,mytime)

# digital colock
Mylabel=Label(root, text='Hello World', font=('Arial',72),fg='white',bg="black")
Mylabel.pack()

mylabel2=Label(root,text="",font=('Arial',24))
mylabel2.pack()
mytime()
#calendar button
btn=Button(root,text=' Pick a date',command=get_date)
btn.pack(pady=10,side=BOTTOM)
# Add calendar
today=Calendar(root,selectmode='day',year=2022,month=3,day=12,fill=BOTH,font=('Arial',24))
today.pack(side=LEFT ,pady=20)
date=Label(root,text=" ",font=('Arial',24))
date.pack(pady=20)

root.mainloop()