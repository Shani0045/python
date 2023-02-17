import cv2 
from tkinter import*
from tkinter import ttk
import os
from tkinter import messagebox
root=Tk()
root.title("Shani")
root.config(bg="lightcyan3")
root.geometry("750x600")
root.resizable(0,0)

label=Label(root,text="Image Extracton Tool",font=("helvetica",23,"bold","underline"),fg="black",bg="lightcyan3")
label.pack()

x=StringVar()
varb1=IntVar()
varb2=IntVar()
var2=IntVar()
var3=StringVar()
def show():
    try:
        v,v=varb1.get(),varb2.get()
        a=x.get()
        x.set("")
        v2=var2.get()
        var2.set("")
        v3=var3.get()
        var3.set("")
        imgs=os.listdir(a)
        clf=cv2.CascadeClassifier('f:/opencv/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')    
        for img in imgs:
            gray=cv2.imread(a +img,v)
            faces=clf.detectMultiScale(gray)
            if(len(faces)>=v2):
                cv2.imwrite(f"{v3}{img}",gray)
            
        messagebox.showinfo("Message","Image Successfully Extract ")
    
            
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        messagebox.showerror("Message","There is a Error in Path")
    
l1=Label(root,text="FROM",font=("helvetica",18,"bold"),fg="black",bg="lightcyan3")
l1.place(x=50,y=100)

e1=Entry(root,textvariable=x,font=("helvetica",16),bd=4)
e1.place(x=230,y=100)

l2=Label(root,text="SELECT",font=("helvetica ",18,"bold"),fg="black",bg="lightcyan3")
l2.place(x=50,y=180)

checkbtn1=Checkbutton(root,text="Color",variable=varb2,font=("helvetica",17),bg="lightcyan3")
checkbtn1.place(x=250,y=175)

checkbtn2=Checkbutton(root,text="GrayScale",variable=varb1,font=("helvetica ",17),bg="lightcyan3")
checkbtn2.place(x=380,y=175)

l3=Label(root,text="NO OF FACES",font=("helvetica",18,"bold"),fg="black",bg="lightcyan3")
l3.place(x=50,y=250)

e3=Entry(root,textvariable=var2,font=("helvetica ",16),bd=4,width=10)

e3.place(x=250,y=250)

l4=Label(root,text="TO",font=("helvetica ",18,"bold"),fg="black",bg="lightcyan3")

l4.place(x=50,y=310)

e4=Entry(root,textvariable=var3,font=("helvetica",16),bd=4)
e4.place(x=250,y=310)

btn2=Button(root,text="Extract Image",font=("helvitica",15),command=show)
btn2.place(x=50,y=400)

btn2=Button(root,text="Quit",font=("helvitica",15),command=root.destroy)
btn2.place(x=260,y=400)

root.mainloop()
