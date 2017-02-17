from tkinter import *

window=Tk()
window.wm_title("Kg converter")

def from_kg():
    gram=float(e2_value.get())*1000
    pound=float(e2_value.get())*2.20462
    ounce=float(e2_value.get())*35.274
    t1.insert(END,gram)
    t2.insert(END,pound)
    t3.insert(END,ounce)
	
# --------------Row 1----------------
e1=Label(window,text="Kg")
e1.grid(row=0,column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=1)

# command = callback function
b1=Button(window,text="Convert",command=from_kg)
b1.grid(row=0,column=2)

# --------------Row 2----------------
t1=Label(window,text="Gram")
t1.grid(row=1,column=0)

t2=Label(window,text="Pound")
t2.grid(row=1,column=1)

t3=Label(window,text="Ounce")
t3.grid(row=1,column=2)

# --------------Row 3----------------
t1=Text(window,height=1,width=20)
t1.grid(row=2,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=2,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=2,column=2)

window.mainloop()