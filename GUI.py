from customtkinter import *
from PIL import Image

root = CTk()
root.geometry("600x350") # window size

set_appearance_mode("dark")



def OnButPress():
    Name.configure(text=field.get()) # Update Label

Titleframe = CTkFrame(master=root)
Titleframe.pack(pady=10,padx=60,fill="both")

# Text
title = CTkLabel(master=Titleframe, text="Hospital Management System",font=("Arial",25),anchor="center")
title.pack(pady=10)

Mainframe = CTkFrame(master=root)
Mainframe.pack(pady=10,padx=60,fill="both",expand = True)


# Button
submitbutton = CTkButton(master=Mainframe,text="Submit", command=OnButPress)
#submitbutton.grid(column=0,row=0)
submitbutton.pack(pady=10)

# Input field
field = CTkEntry(master=Mainframe)
#field.grid(column=0,row=0)
field.pack(pady=10)

Name = CTkLabel(master=Mainframe, text="-")
Name.pack()


root.mainloop()