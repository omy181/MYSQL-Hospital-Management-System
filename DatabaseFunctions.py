import pandas as pd
import DatabaseManager as db


TableValues = {
    "Doctor": {
        "ID":"Doctor_ID",
        "Values":"(First_Name,Last_Name,Department,Specialty)",
        "Count":4,
        "Default":("First_Name","Last_Name","Department","Specialty")
    },
    "Patient": {
        "ID":"Patient_ID",
        "Values":"(First_Name,Last_Name,Phone_Number,Adress,Date_of_birth,Email)",
        "Count":6,
        "Default":("First_Name","Last_Name",0,"Adress","Date_of_birth","Email")
    },    
    "Appointment": {
        "ID":"Appointment_ID",
        "Values":"(Doctor_ID,Patient_ID,Date,Time,Location)",
        "Count":5,
        "Default":(2,2,"Date","Time","Location")
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

def ListTable(table_name):
    li = []
    hs = []

    for row in db.Select(f"SHOW COLUMNS FROM {table_name}"):
        hs.append(row[0])

    for index,row in enumerate(db.Select(f"select * from {table_name}")):
        li.append([])
        for feature in row:
            li[index].append(feature)
    return hs,li    

#db.mydb.close()