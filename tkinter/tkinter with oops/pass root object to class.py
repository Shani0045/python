from tkinter import*
from tkinter.tix import Form
from turtle import width
class NumberPlate:
    def __init__(self,master):
        self.master=master
        self.width=995
        self.height=610
        start_window_from_x_axis=(self.master.winfo_screenwidth()//2)-(self.width//2)
        start_window_from_y_axis=(self.master.winfo_screenheight()//3)-(self.height//3)
        self.master.title("Driver Detection")
        self.master.geometry(f"{self.width}x{self.height}+{start_window_from_x_axis}+{start_window_from_y_axis}")
        self.master.resizable(0,0)
        # self.iconbitmap(r"images/logo.ico")
        self.ui()
    def ui(self):
        self.header_frame=Frame(self.master,bd=2,relief=RIDGE)
        self.header_frame.place(x=0,y=0,width=994,height=100)
        
        self.label=Label(self.header_frame,text="Hello world")
        self.label.place(x=10,y=10)

        self.form_frame=Frame(self.master,bd=2,relief=RIDGE)
        self.form_frame.place(x=0,y=100,width=500,height=300)
        
        self.label2=Label(self.form_frame,text="Hello world")
        self.label2.place(x=10,y=10)
        
        self.btn=Button(self.form_frame,text="clickme",command=self.click)
        self.btn.place(x=10,y=50)

        self.table_frame=Frame(self.master,bd=2,relief=RIDGE)
        self.table_frame.place(x=500,y=100,width=493,height=300)

    def click(self):
        print("button clicked")


if __name__=="__main__":
    root=Tk()
    app=NumberPlate(root)
    root.mainloop()