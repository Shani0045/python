#___________________________________________import all requeired library_____________________________________
from io import BytesIO
from tkinter import*
from PIL import ImageTk,Image
import cv2
import easyocr
from tkinter import messagebox
import threading
import arrow
import pickle
import psycopg2
import base64
from io import BytesIO
import pickle
import numpy as np
import face_recognition as fc
from tensorflow.keras.preprocessing.image import load_img,img_to_array,array_to_img
from tensorflow.keras.models import load_model
from configparser import ConfigParser
reader = easyocr.Reader(['en'])
model=load_model("custommodel/truck-model-12.h5")
#________________________________________Main class_____________________________________________________________
class NumberPlate:
    def __init__(self,root):
        self.root=root
        self.initUI()
    def initUI(self):
#__________________________________________________Window initialization_________________________________________
        self.width=853
        self.height=520
        self.start_window_from_x_axis=(self.root.winfo_screenwidth()//2)-(self.width//2)
        self.start_window_from_y_axis=(self.root.winfo_screenheight()//3)-(self.height//3)
        self.root.title("PlateNumberDetection")
        self.root.iconbitmap(r"img/logo.ico")
        self.root.geometry(f"{self.width}x{self.height}+{self.start_window_from_x_axis}+{self.start_window_from_y_axis}")
        self.root.resizable(0,0)
#_______________________________ header frame __________________________________________________________________
        self.header_frame=Frame(self.root,bg="#0095FF")
        self.header_frame.place(x=0,y=0,width=853,height=95)
        self.load_top_img=Image.open("img/truck1.png")
        self.resize_top_img=self.load_top_img.resize((100,60))
        self.top_img=ImageTk.PhotoImage(self.resize_top_img)
        self.top_img_label=Label(self.header_frame,bd=0,image=self.top_img,bg="#0095FF")
        self.top_img_label.place(x=10,y=10)
        self.title_label=Label(self.header_frame,text="VEHICLE PLATE RECOGNITION SYSTEM",font=("arial 14"),bg="#0095FF",fg="white")
        self.title_label.pack(pady=12)
        self.screen_label=Label(self.header_frame,text="Detect Plate Number",font=("arial 12 bold"),bg="#0095FF",fg="white")
        self.screen_label.pack(pady=3)      
#______________________________form frame ________________________________________________________________________
        self.vehicle_frame=LabelFrame(self.root,text="Vehicle Details",bd=2,relief=RIDGE,width=480,height=85)
        self.vehicle_frame.place(x=5,y=100)

        self.lblVehicle=Label(self.vehicle_frame,text="Vehicle No.",font=("arial 12"))
        self.lblVehicle.place(x=25,y=15)
        self.vehicleVar=StringVar()
        self.vehicleEntry=Entry(self.vehicle_frame,textvariable=self.vehicleVar,font=("arial 12"),width=20,highlightbackground="gray", highlightthickness=0.5, bd=0,state=DISABLED)
        self.vehicleEntry.place(x=150,y=15)

        self.form_frame=LabelFrame(self.root,text="Driver Details",bd=2,relief=RIDGE,width=480,height=294)
        self.form_frame.place(x=5,y=190)
        self.Dname=Label(self.form_frame,text="Driver Name",font=("arial 12"))
        self.Dname.place(x=25,y=15)
        self.driverVar=StringVar()
        self.DnameEntry=Entry(self.form_frame,textvariable=self.driverVar,font=("arial 12"),width=20,highlightbackground="gray", highlightthickness=0.5, bd=0,state=DISABLED)
        self.DnameEntry.place(x=150,y=15)

        self.photo_frame=Frame(self.form_frame,bd=2,relief=RIDGE,height=105,bg="white",width=110)
        self.photo_frame.place(x=350,y=15)

        self.load_img=Image.open("img/no-profile.jpg")
        self.resize_img=self.load_img.resize((105,100))
        self.img=ImageTk.PhotoImage(self.resize_img)
        self.img_label=Label(self.photo_frame,bd=0,image=self.img,bg="#0095FF")
        self.img_label.place(x=0,y=0)

        self.lblDL=Label(self.form_frame,text="DL No.",font=("arial 12"))
        self.lblDL.place(x=25,y=50)
        self.dlVar=StringVar()
        self.DLEntry=Entry(self.form_frame,textvariable=self.dlVar,font=("arial 12"),width=20,highlightbackground="gray", highlightthickness=0.5, bd=0,state=DISABLED)
        self.DLEntry.place(x=150,y=50)

        self.lbl_DLexp=Label(self.form_frame, text="DL Expiry",font=("Ariel",12), )
        self.lbl_DLexp.place(x=25, y=85)
        self.dlexpVar=StringVar()
        self.txt_DLexp=Entry(self.form_frame,font=("Ariel",12),textvariable=self.dlexpVar ,highlightbackground="gray", highlightthickness=0.5, bd=0,state=DISABLED)
        self.txt_DLexp.place(x=150, y=85)

        self.lbl_Mob=Label(self.form_frame, text="Mobile", font=("Ariel",12), )
        self.lbl_Mob.place(x=25, y=120)
        self.mobVar=StringVar()
        self.txt_Mob=Entry(self.form_frame,font=("Ariel",12),textvariable=self.mobVar, highlightbackground="gray", highlightthickness=0.5, bd=0,state=DISABLED)
        self.txt_Mob.place(x=150, y=120)

        self.lbl_act=Label(self.form_frame, text=" Is Active", font=("Ariel",12), )
        self.lbl_act.place(x=25, y=155)
        self.chkbx = Checkbutton(self.form_frame, onvalue="true", offvalue="false",state=DISABLED)
        self.chkbx.place(x=145, y=155)

        self.DAddrs=Label(self.form_frame,text="Driver Address",font=("arial 12"))
        self.DAddrs.place(x=25,y=190)
        self.addressVar=StringVar()
        self.txt_Addr=Text(self.form_frame,font=("Ariel",12), bg="white", highlightbackground="gray", highlightthickness=0.5, bd=0,state=DISABLED)
        self.txt_Addr.place(x=150, y=190, height=70, width=320)
#____________________________right frame & camera frame______________________________________________________________  
        self.right_frame=LabelFrame(self.root,text="Camera",relief=RIDGE,height=350,width=360)
        self.right_frame.place(x=488,y=99)
        now=arrow.now().format("DD-MM-YYYY")
        self.camera_frame=Frame(self.right_frame,bd=2,relief=RIDGE,height=280,bg="white",width=346)
        self.camera_frame.place(x=5,y=0)
        self.lbl_photo = Label(self.camera_frame,bd=2,bg="white")
        self.lbl_photo.place(x=0,y=0)
        self.nplateBtn=Button(self.right_frame,text="Detect Truck No",font=("arial 10 bold"),width=13,bg="#0095FF",fg="white",relief=RIDGE,command=self.numberPlateDetectThread)
        self.nplateBtn.place(x=235,y=290)
        self.checktruckBtn=Button(self.right_frame,text="Check Truck",font=("arial 10 bold"),width=12,bg="#0095FF",fg="white",relief=RIDGE,command=self.checkTruckThread)
        self.checktruckBtn.place(x=121,y=290)
        self.driverBtn=Button(self.right_frame,text="Detect Driver",font=("arial 10 bold"),width=12,bg="#0095FF",fg="white",relief=RIDGE,command=self.detectCamera)
        self.driverBtn.place(x=6,y=290)
#______________________________ footer frame _________________________________________________________________
        self.footer_frame=Frame(self.root,bg="#DCDCDC",height=35)
        self.footer_frame.pack(side=BOTTOM,fill=BOTH)
        self.lblTranzol=Label(self.footer_frame,text="T R A N Z O L",font=("arial 12"),bg="#DCDCDC",fg="#0095FF")
        self.lblTranzol.place(x=10,y=6)

#_________________________________database connectivity_______________________________________________________
    def connectdb(self):
        config=ConfigParser()
        config.read("config.ini")
        db=config['database']
        dbname=db['name']
        user=db['user']
        password=db['password']
        host=db['host']
        port=db['port']
        connection=psycopg2.connect(database=dbname,user=user,password=password,host=host,port=port)
        cursor=connection.cursor()
        return connection,cursor
#______________________________________open camera and detect vehicle number___________________________________
    def numberPlateDetectThread(self):
        if self.nplateBtn["text"]=="Detect Truck No":
            self.nplateBtn.config(text="Stop",bg="red")
            thread=threading.Thread(target=self.numberPlateDetect)
            thread.start()
        else:
            self.nplateBtn.config(text="Detect Truck No",bg="#0095FF")
            self.stopNPlateCamera()

    def numberPlateDetect(self):
        try:
            self.cap = cv2.VideoCapture(cv2.CAP_DSHOW)
            def camera():
                self.var=None
                self.lbl_photo.place(x=0,y=0)
                success, frame = self.cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                plate_detector = cv2.CascadeClassifier("custommodel/haarcascade_russian_plate_number.xml")
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image)
                detections = plate_detector.detectMultiScale(gray, scaleFactor=2.06, minNeighbors=7)
                for (x, y, w, h) in detections:
                    number_plate = gray[y:y + h, x:x + w]
                    number_plate=cv2.fastNlMeansDenoising(number_plate,31, 7, 21)
                    read = reader.readtext(number_plate,decoder="beamsearch")
                    try:
                        if round(read[0][-1],2)>0.8:
                            self.var=round(read[0][-1],2)
                            self.vehicleVar.set(read[0][-2].upper())
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255,0), 2)
                            cv2.putText(frame, read[0][-2].upper(), (x - 20, y - 10),cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255,0), 2)
                            
                    except:
                        pass
                imgtk = ImageTk.PhotoImage(image=img.resize((380,280)))
                self.lbl_photo.imgtk = imgtk
                self.lbl_photo.configure(image=imgtk)
                self.lbl_id=self.lbl_photo.after(15,camera)
                if self.var is not None:
                    self.nplateBtn.config(text="Detect Truck No",bg="#0095FF")
                    self.stopNPlateCamera()
            camera()
        except Exception as e:
            messagebox.showerror("Error","Please check webcam is not connected!")

    def stopNPlateCamera(self):
        self.lbl_photo.after_cancel(self.lbl_id)
        self.cap.release()
        cv2.destroyAllWindows()
        self.lbl_photo.place_forget()
#___________________________________________________detect driver image______________________________________________________

    def detectCamera(self):
        if self.driverBtn["text"]=="Detect Driver":
            self.driverBtn.config(text="Stop",bg="red")
            thread=threading.Thread(target=self.driverDetect)
            thread.start()
        else:
            self.driverBtn.config(text="Detect Driver",bg="#0095FF")
            self.detectCancel()

    def driverDetect(self):
        try:
            self.cam=cv2.VideoCapture(cv2.CAP_DSHOW)
            conn,cur=self.connectdb()
            cur.execute("select modeldata from facedetection")
            dt=cur.fetchone()
            decoded_str=base64.b64decode(dt[0])
            data=pickle.loads(decoded_str)
            encoded_list_known=data["datapoints"]
            classname=data["class"]
            self.lbl_photo.place(x=0,y=0)
            self.name=None
            def camera():
                success,img=self.cam.read()
                res=cv2.resize(img,(500,500))
                color=cv2.cvtColor(res,cv2.COLOR_RGB2BGR)
                imgS=cv2.resize(res,(0,0),None,0.25,0.25)
                imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
                face_location=fc.face_locations(imgS)
                face_encoding=fc.face_encodings(imgS,face_location)
                for encodeface,faceloc in zip(face_encoding,face_location):
                    matches=fc.compare_faces(encoded_list_known,encodeface,tolerance=0.5)    # value set less than 0.6 for more strict
                    face_dist=fc.face_distance(encoded_list_known,encodeface)
                    matchindex=np.argmin(face_dist)
                    if matches[matchindex]:
                        self.name=classname[matchindex].upper()
                        y1,x2,y2,x1=faceloc
                        y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                        cv2.rectangle(color,(x1,y1),(x2+30,y2+50),(0,255,0),2)      # rectangle for face
                        cv2.rectangle(color,(x1,y2+50),(x2+30,y2),(0,255,0),cv2.FILLED)  # rectangle for text
                        cv2.putText(color,self.name,(x1+12,y2+35),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,255,255),2)
                    else:
                        self.name="Unknown"
                        y1,x2,y2,x1=faceloc
                        y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                        cv2.rectangle(color,(x1,y1),(x2+30,y2+50),(255,0,0),2)      # rectangle for face
                        cv2.rectangle(color,(x1,y2+50),(x2+30,y2),(255,0,0),cv2.FILLED)  # rectangle for text
                        cv2.putText(color,self.name,(x1+12,y2+35),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,255,255),2)

                img = Image.fromarray(np.fliplr(color))
                imgtk = ImageTk.PhotoImage(image=img.resize((370,280)))
                self.lbl_photo.imgtk = imgtk
                self.lbl_photo.configure(image=imgtk)    
                self.lbl_id=self.lbl_photo.after(12,camera)
                try:
                    if self.name!="Unknown" and self.name is not None:
                        self.driverBtn.config(text="Detect Driver",bg="#0095FF")
                        self.detectCancel()
                        self.name="Unknown"
                except Exception as e:
                    pass
            camera()
        except Exception as e:
            self.driverBtn.config(text="Detect Driver",bg="#0095FF")
            messagebox.showerror("Error","Please check, webcam is not connected or there is no data for detection.")
                                                                                                
    def detectCancel(self):
        self.lbl_photo.after_cancel(self.lbl_id)
        self.cam.release()
        cv2.destroyAllWindows()
        self.lbl_photo.place_forget()
        dlno=self.name
        connection,cursor=self.connectdb()
        cursor.execute(f"select * from drivers inner join driversimage on drivers.driverid=driversimage.driverid where dlno='{dlno.upper()}'")
        row=cursor.fetchone()
        self.driverVar.set(row[1])
        self.dlVar.set(row[2])
        date=arrow.get(row[5])
        self.dlexpVar.set(date.format("DD-MM-YYYY"))
        self.mobVar.set(row[7])
        self.txt_Addr.delete('1.0',END)
        if row[4] is None:
            self.txt_Addr.insert(END,"")
        else:
            self.txt_Addr.insert(END,row[4])
        if row[6]=="true" or row[6]==True:
            self.chkbx.select()
        else:
            self.chkbx.deselect()
#____________________________________________Place image in photo frame___________________________________________________________
        try:
            self.decoded_img=base64.b64decode(row[-1])
            self.bytes_data=BytesIO(self.decoded_img)
            self.img_photo= Image.open(self.bytes_data)
            self.img_res=self.img_photo.resize((108,102))
            self.photo_img = ImageTk.PhotoImage(self.img_res)
            self.img_label.configure(image=self.photo_img)
            self.img_label.image=self.photo_img
        except Exception as e:
            img_photo= Image.open("img/no-profile.jpg")
            img_res=img_photo.resize((108,102))
            self.photo_img = ImageTk.PhotoImage(img_res)
            self.img_label.configure(image=self.photo_img)
            self.img_label.image=self.photo_img

    def checkTruckThread(self):
        if self.checktruckBtn["text"]=="Check Truck":
            self.checktruckBtn.config(text="Stop",bg="red")
            thread=threading.Thread(target=self.checkTruck)
            thread.start()
        else:
            self.checktruckBtn.config(text="Check Truck",bg="#0095FF")
            self.stopTruckcamera()

    def checkTruck(self):
        try:
            self.cap = cv2.VideoCapture(cv2.CAP_DSHOW)
            def camera():
                self.lbl_photo.place(x=0,y=0)
                success, frame = self.cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                resize=cv2.resize(frame,(224,224))
                test_img=resize/255
                test_img=np.expand_dims(test_img,0)
                pred=model.predict(test_img,use_multiprocessing=True)
                pred=np.argmax(pred,1)
                if pred[0]==1:
                    cv2.putText(frame,"Loaded Truck", (13,30),cv2.FONT_HERSHEY_TRIPLEX,0.8,(0,255,0),2)
                elif pred[0]==0:
                    cv2.putText(frame,"Empty Truck", (13,30),cv2.FONT_HERSHEY_TRIPLEX,0.8,(255,0,0),2)
                img = Image.fromarray(frame)   
                imgtk = ImageTk.PhotoImage(image=img.resize((380,280)))
                self.lbl_photo.imgtk = imgtk
                self.lbl_photo.configure(image=imgtk)
                self.lbl_id=self.lbl_photo.after(15,camera)
            camera()
        except Exception as e:
            messagebox.showerror("Error","Please check webcam is not connected!")

    def stopTruckcamera(self):
        self.lbl_photo.after_cancel(self.lbl_id)
        self.cap.release()
        cv2.destroyAllWindows()
        self.lbl_photo.place_forget()
        
def main():
    root=Tk()
    app=NumberPlate(root)
    root.mainloop()
    
if __name__=="__main__":
    main()
    
