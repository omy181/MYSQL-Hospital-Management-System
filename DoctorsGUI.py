from customtkinter import *
from CTkTable import *
import DatabaseFunctions as dbf

def DeleteRecord():
    return

def OpenWindow(root):
    window = CTkToplevel(root)
    window.title("Doctors")
    window.geometry("600x350")
    
    window.columnconfigure(0,1)
    window.columnconfigure(1,10)

    data = dbf.ListDoctors()

    #SQLList = CTkTable(master=window,row=len(data), column=len(data[0]), values=data)
    #SQLList.pack(expand=False, fill="both", padx=20, pady=20)

    DeleteButton = CTkButton(master=window,text="Delete", command=DeleteRecord)
    DeleteButton.grid()
    DeleteButton.pack(padx=20, pady=20)