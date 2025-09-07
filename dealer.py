
import customtkinter
import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode

app=customtkinter.CTk()
app.title("Dealer Dashboard")
app.geometry("1920x1080")


label1=customtkinter.CTkLabel(app,text="Customer Name :",font=('arial',20,'bold'),fg_color='white')
label1.place(x=50,y=80)

label2=customtkinter.CTkLabel(app,text="Aadhar No.         :",font=('arial',20,'bold'),fg_color='white')
label2.place(x=50,y=120)

label3=customtkinter.CTkLabel(app,text="Bill                      :",font=('arial',20,'bold'),fg_color='white')
label3.place(x=50,y=160)

bill = 10

upi = "rahulovhal25@ybl"




app.mainloop()