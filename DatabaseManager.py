import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456Ab",
  database="HospitalData"
)

def ExecuteQuerryWithValues(querry,values):
    #Example
    #sql = "insert into Patient (First_Name,Last_Name) values (%s,%s);"
    #val = ("omyy","oiiii")
    
    mycursor = mydb.cursor()

    mycursor.execute(querry,values)
    mydb.commit()

    mycursor.close()

def ExecuteQuerry(querry):  
    mycursor = mydb.cursor()

    mycursor.execute(querry)
    mydb.commit()

    mycursor.close()

def Select(querry):
    # "select * from `Doctor`"
    mycursor = mydb.cursor()
    mycursor.execute(querry)
    myresult = mycursor.fetchall()
    return myresult








