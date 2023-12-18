from customtkinter import *
import DoctorsGUI
import PatientsGUI
from PIL import Image

root = CTk()
root.title("Hospital Management System")
root.geometry("600x350") # window size

set_appearance_mode("dark")



def GoToPatients():
    PatientsGUI.OpenWindow(root)
    return
    #Name.configure(text=field.get()) # Update Label

def GoToDoctors():
    DoctorsGUI.OpenWindow(root)
    return

Titleframe = CTkFrame(master=root)
Titleframe.pack(pady=10,padx=60,fill="both")

# Text
title = CTkLabel(master=Titleframe, text="Hospital Management System",font=("Arial",25),anchor="center")
title.pack(pady=10)

Mainframe = CTkFrame(master=root)
Mainframe.pack(pady=10,padx=60,fill="both",expand = True)


# Button
PatinetButton = CTkButton(master=Mainframe,text="Patients", command=GoToPatients)
#submitbutton.grid(column=0,row=0)
PatinetButton.pack(pady=10)

# Button
PatinetButton = CTkButton(master=Mainframe,text="Doctors", command=GoToDoctors)
#submitbutton.grid(column=0,row=0)
PatinetButton.pack(pady=10)


"""
# Input field
field = CTkEntry(master=Mainframe)
#field.grid(column=0,row=0)
field.pack(pady=10)

Name = CTkLabel(master=Mainframe, text="-")
Name.pack()
"""

root.mainloop()