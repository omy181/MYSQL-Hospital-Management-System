import pandas as pd
import DatabaseManager as db


TableValues = {
    "Doctor": {
        "ID":"Doctor_ID",
        "Values":"(First_Name,Last_Name,Department,Specialty)",
        "Count":4,
        "Default":("First_Name","Last_Name","Department","Specialty"),
    },
    "Patient": {
        "ID":"Patient_ID",
        "Values":"(First_Name,Last_Name,Phone_Number,Adress,Date_of_birth,Email)",
        "Count":6,
        "Default":("First_Name","Last_Name",0,"Adress",db.datetime.now().date(),"Email"),
        "Date":("Date_of_birth")
    },    
    "Appointment": {
        "ID":"Appointment_ID",
        "Values":"(Doctor_ID,Patient_ID,Date,Time,Location)",
        "Count":5,
        "Default":(2,2,db.datetime.now().date(),db.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"Location"),
        "Date":("Date")
    },
    "Medical_Prescription": {
        "ID":"Prescription_ID",
        "Values":"(Patient_ID,Doctor_ID,Medication_Name,Dosage,Instructions,Diagnosis)",
        "Count":6,
        "Default":(2,2,"Medication Name","Dosage","Instructions","Diagnosis")
    } 
    }

# Elementary Functions

def AddNewRecord(table_name):

    attribute_count = TableValues[table_name]["Count"]
    values_to_add = TableValues[table_name]["Values"]
    values = TableValues[table_name]["Default"]
    vals = ""
    for _ in range(attribute_count-1):
        vals += "%s,"
    vals += "%s"

    sql = f"insert into {table_name} {values_to_add} values ({vals});"
    db.ExecuteQuerryWithValues(sql,values)

def RemoveRecord(table_name,id):    
    table_id_name = TableValues[table_name]["ID"]
    sql = f"delete from {table_name} where {table_id_name} = {id};"
    db.ExecuteQuerry(sql)

def UpdateRecord(table_name,id,valuetochange,newvalue): 
    table_id_name = TableValues[table_name]["ID"]   
    sql = f"update {table_name} set {valuetochange} = '{newvalue}' where {table_id_name} = {id};"
    try:
        db.ExecuteQuerry(sql)
        return True
    except:       
        print("Could not Update Record")
        return False

def GetRecordCount(table_name):
    table_id_name = TableValues[table_name]["ID"]
    sql = f"select count({table_id_name}) from {table_name};"
    return db.Select(sql)[0][0]


def GetMinMaxRecord(table_name,minstate = "min"):
    column = TableValues[table_name]["Date"]
    table_id_name = TableValues[table_name]["ID"]
    sql = f"select {table_id_name},{column} FROM {table_name} where {column} = (select {minstate}({column}) from {table_name});"
    return db.Select(sql)[0]

def ListTable(table_name,orderby_type = -1):

    if orderby_type == -1:
        orderby_type = TableValues[table_name]["ID"]
    li = []
    hs = []

    for row in db.Select(f"SHOW COLUMNS FROM {table_name}"):
        hs.append(row[0])

    for index,row in enumerate(db.Select(f"select * from {table_name} order by {orderby_type}")):
        li.append([])
        for feature in row:
            li[index].append(feature)
    return hs,li    

#   Custom Functions

def GetMostAppointedDoctor():
    table_id_name = TableValues["Doctor"]["ID"]
    sql = f"SELECT {table_id_name}, COUNT(*) AS appointment_count FROM Appointment GROUP BY {table_id_name} ORDER BY appointment_count DESC LIMIT 1;"
    return db.Select(sql)[0]

def GetAveragePatientAge():
    sql = f"SELECT AVG(YEAR(CURDATE()) - YEAR(Date_of_birth)) AS average_age FROM Patient;"
    return db.Select(sql)[0][0]

def GetOldestYoungestPatientAge(minstate = "min"):
    sql = f"select Patient_ID,YEAR(CURDATE()) - YEAR(Date_of_birth) as AGE FROM Patient where YEAR(Date_of_birth) = (select {minstate}(YEAR(Date_of_birth)) from Patient);"
    return db.Select(sql)[0]

#db.mydb.close()