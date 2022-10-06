
import tkinter


from tkinter import *
from tkinter import StringVar
from PIL import Image,ImageTk 
import qrcode

def create_qrcode(): 
    
    text = qr_text.get()
    print(text)
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color='white')
    img.show() 

if __name__ == '__main__':

    #=== สร้างหน้าจอ 
    root = Tk()
    #==== ชื่อหน้าจอ  
    root.title("BNC Project")
    root.geometry("400x500+0+0")
    root.iconbitmap("img/facebook.ico")
    root.config(bg='pink')

    logo = Image.open("img/logo.png").resize((250,250))
    logo_label = ImageTk.PhotoImage(logo)

    app_header = Label(root,text="QRCode Generator",bg='pink',fg='black',font=("Comic sans MS",20,"bold","underline","italic"),cursor='hand2')
    app_header.pack()

    Label(root,image=logo_label,bg='pink').pack()
    
    qr_text = StringVar() 
    ent = Entry(root,textvariable=qr_text,width=50)
    ent.pack(ipady=10,pady=10)

    submit_btn = Button(root,text="Generate",width=10,height=2,command=create_qrcode,bg='black',fg='white',cursor='hand2')
    submit_btn.pack()

    root.mainloop()

