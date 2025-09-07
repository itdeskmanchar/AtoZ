import customtkinter
from PIL import Image,ImageTk

app = customtkinter.CTk()
app.title("my app")
app.geometry("400x180")
lab1= customtkinter.CTkLabel(app, text=" A to Z multiservices ",font=("monotype corsiva",90,"bold"), bg_color="white")
lab1.place(x=500, y=20)

image = Image.open("atoz.jpg")
resize = image.resize((330, 330))  
photo_images = ImageTk.PhotoImage(resize)
image_label = customtkinter.CTkLabel(app,text="",image=photo_images)
image_label.place(x=10, y=10)

lab2=customtkinter.CTkLabel(app, text="Role:",font=("arial",30,"bold"),bg_color="white" )
lab2.place(x=600, y=400)
entry = customtkinter.CTkEntry(app,font=("arial",25,"bold"),width=300)
entry.place(x=780,y=400)
customtkinter.set_appearance_mode("light")

lab2=customtkinter.CTkLabel(app, text="Email:",font=("arial",30,"bold"),bg_color="white")
lab2.place(x=600, y=500)
entry = customtkinter.CTkEntry(app,font=("arial",25,"bold"),width=300)
entry.place(x=780,y=500)

lab2=customtkinter.CTkLabel(app, text="Password:",font=("arial",30,"bold"), bg_color="white" )
lab2.place(x=600, y=600)
entry = customtkinter.CTkEntry(app,font=("arial",25,"bold"),width=300, show="*")
entry.place(x=780,y=600)

def button_event():
    entered_pass = entry.get()
    if entered_pass == "sanika123":
        print("✅ Login successful")
    else:
        print("❌ Incorrect password")


def button_pressed():
    print("button pressed")

button = customtkinter.CTkButton(app, text="Login", command=quit)
button.place(x=800,y=700)

app.mainloop()