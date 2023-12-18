from customtkinter import *
from CTkTable import *
import DatabaseFunctions as dbf

def OpenWindow(root):
    window = CTkToplevel(root)
    window.title("Patients")
    window.geometry("800x350")
    
    data = dbf.ListPatients()

    SQLList = CTkTable(master=window,row=len(data), column=len(data[0]), values=data)
    SQLList.pack(expand=False, fill="both", padx=20, pady=20)