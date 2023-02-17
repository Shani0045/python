from tkinter import*
from tkinter.tix import Form
from turtle import width
class NumberPlate(Tk):
    def __init__(self):
        super().__init__()
        self.width=995
        self.height=610
        start_window_from_x_axis=(self.winfo_screenwidth()//2)-(self.width//2)
        start_window_from_y_axis=(self.winfo_screenheight()//3)-(self.height//3)
        self.title("Driver Detection")
        self.geometry(f"{self.width}x{self.height}+{start_window_from_x_axis}+{start_window_from_y_axis}")
        self.resizable(0,0)
        # self.iconbitmap(r"images/logo.ico")
        self.ui()

    def ui(self):
        
        self.header_frame=Frame(self,bd=2,relief=RIDGE)
        self.header_frame.place(x=0,y=0,width=994,height=100)
        
        self.config(bg="pink")
        
        self.label=Label(self.header_frame,text="Hello world")
        self.label.place(x=10,y=10)

        self.form_frame=Frame(self,bd=2,relief=RIDGE)
        self.form_frame.place(x=0,y=100,width=500,height=300)
        
        self.label2=Label(self.form_frame,text="Hello world")
        self.label2.place(x=10,y=10)
        
        self.btn=Button(self.form_frame,text="clickme",command=self.click)
        self.btn.place(x=10,y=50)
        self.btn.bind("<Enter>",self.hover)
        self.btn.bind("<Button-1>",self.textchange)

        self.table_frame=Frame(self,bd=2,relief=RIDGE)
        self.table_frame.place(x=500,y=100,width=493,height=300)

    def click(self):
        print("button clicked")

    def hover(self,evnt):
        self.btn.config(bg="pink")
    def textchange(self,evnt):
        self.btn.config(text="Submit")

if __name__=="__main__":
    root=NumberPlate()
    root.mainloop()
