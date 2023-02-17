from tkinter import *
root=Tk()
root.geometry("900x550")
root.title("gmail.com")
root.config(bg="sky blue")
def login():
     import smtplib as sm
     try:
          server=sm.SMTP("smtp.gmail.com",587)
          server.starttls()
          a=e1.get()
          b=e2.get()
          server.login(a,b)
          c=e3.get()
          d=e4.get()
          e=msg.get("1.0","end-1c")
          send=server.sendmail(c,d,e)
          server.quit()
          print("Message Send Successfully")
          
     except:
          print("Message Not Send")
     
          
          
     
     
#second _____________________________________________________________

label=Label(root,text=" Welcome To Gmail " ,font=("Times new roman",25,"bold","underline"),bg="sky blue",fg="black").pack() 
l3=Label(root,text="Sender-Email",font=("times new roman",17),bg="sky blue",fg="black")
l3.place(x=15,y=140)
e3=Entry(root,font=("Arial",15),width=25)
e3.place(x=180,y=140)
l4=Label(root,text="Receiver-Email",font=("times new roman",17),bg="sky blue",fg="black")
l4.place(x=15,y=180)
e4=Entry(root,font=("Arial",15),width=25)
e4.place(x=180,y=180)
l5=Label(root,text="Message",font=("times new roman",17),bg="sky blue",fg="black")
l5.place(x=15,y=220)
msg=Text(root,font=("Arial",14),width=35,height=6)
msg.place(x=180,y=220)
btn=Button(root,text="Send",font=("times new roman",17),command=login)
btn.place(x=180,y=360)
btn=Button(root,text="Quit",font=("times new roman",17),command=root.destroy)
btn.place(x=250,y=360)

# first______________________________________________________________
l1=Label(root,text="Email id",font=("times new roman",17),bg="sky blue",fg="black")
l1.place(x=15,y=60)
e1=Entry(root,font=("times new roman",17),width=25)
e1.place(x=180,y=60)
l2=Label(root,text="password",font=("times new roman",17),bg="sky blue",fg="black")
l2.place(x=15,y=100)
e2=Entry(root,font=("times new roman",17),show="*",width=25)
e2.place(x=180,y=100)
















root.mainloop()
