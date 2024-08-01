from tkinter import *
t=Tk()
t.geometry('2000x2000')
t.config(bg='sky blue')
t.title("First application")

def login():
    print("connecting to database..")
    

l1= Label(t,text="Register for our application",font=("times",20,"bold")).place(x=500,y=50)
l2= Label(t,text="User id",font=("times",20,"bold")).place(x=450,y=150)
e1=Entry(t,font=("times",20,"bold")).place(x=650,y=150)

l3= Label(t,text="password",font=("times",20,"bold")).place(x=450,y=200)
e1=Entry(t,show=".",font=("times",20,"bold")).place(x=650,y=200)

b1=Button(t,text= "Login",font=("times",20,"bold"),fg="purple",command=login).place(x=450,y=300)
b2=Button(t,text= "reset",font=("times",20,"bold"),fg="purple").place(x=650,y=300)
b3=Button(t,text= "forgot password?",font=("times",20,"bold"),fg="purple").place(x=800,y=300)




