import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="minecraft172",
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
    # "select * from Patients where ---"
    mycursor = mydb.cursor()
    mycursor.execute(querry)
    myresult = mycursor.fetchall()

    return myresult








