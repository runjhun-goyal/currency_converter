from tkinter import *

root=Tk()
OPTIONS={
    "Australlian Dollar":49.10,
    "Brazillian Real":17.30,
    "British Pound":90.92,
    "Bulgarian Lev":39.8,
    "Chinese Yuan":10.29,
    "Euro":77.85,
    "Hongkong Dollar":8.83,
    "Indonasian Rupiah":0.004864,
    "Japanese Yen":0.628,
    "Pakistani Rupee":0.49,
    "Shrilankan Rupee":0.39,
    "Swis Franc":69.62,
    "US Dollar":69.32,
    
}
def con():
    indian=e1.get()
    ans=variable.get()
    var=OPTIONS.get(ans,None)
    finalans=float(indian)/float(var)
    res.delete(1.0,END)
    res.insert(INSERT,finalans)
def reset():
    res.delete(1.0,END)
    e1.delete(0,END)
    
    

root.geometry("700x700+10+10")
root.title("currency converter")
root.config(background='black')
root.resizable(0,0)

Label(root,text="INDIAN RUPPEES :",bg="black",fg="white",font=("arial",16,"bold")).place(x=60,y=130)
e1=Entry(root,font=("calibri",20))
e1.place(x=260,y=130)
Label(root,text="CONVERTED AMOUNT:",bg="black",fg="red",font=("arial",16,"bold")).place(x=10,y=270)
Label(root,text="CURRENCY CONVERTER",bg="black",fg="blue",font=("comicsansms", 40 ,"bold","underline"),padx=20,pady=20).grid(row=0,column=0)
res=Text(root, height=4,width=40,bg="pink",fg="blue",relief=SUNKEN,borderwidth=5,font=("arial",12))
res.place(x=250,y=250)
variable=StringVar(root)
variable.set(None)
OptionMenu(root,variable,*OPTIONS).place(x=450,y=350)
Label(root,text="CHOOSE CURRENCY :",bg="black",fg="white",font=("arial",16,"bold")).place(x=60,y=350)
Button(root,text="CONVERT",bg="white",fg="red",height=2,width=15,relief=RIDGE,borderwidth=3,font=("calibri",20),command=con).place(x=100,y=500)
Button(root,text="RESET",bg="white",fg="red",height=2,width=15,relief=RIDGE,borderwidth=3,font=("calibri",20),command=reset).place(x=350,y=500)
root.mainloop()