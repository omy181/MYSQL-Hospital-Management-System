import pandas as pd
import DatabaseManager as db

# Elementary Functions

def AddNewRecord(table_name,attribute_count,values_to_add,values):
    vals = ""
    for _ in range(attribute_count-1):
        vals += "%s,"
    vals += "%s"

    sql = f"insert into {table_name} {values_to_add} values ({vals});"
    db.ExecuteQuerryWithValues(sql,values)

def RemoveRecord(table_name,table_id_name,id):    
    sql = f"delete from {table_name} where {table_id_name} = {id};"
    db.ExecuteQuerry(sql)

def UpdateRecord(table_name,table_id_name,id,valuetochange,newvalue):    
    sql = f"update {table_name} set {valuetochange} = {newvalue} where {table_id_name} = {id};"
    db.ExecuteQuerry(sql)

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

# Custom Functions

# ---------------------Patient
def AddNewPatient(value):
    AddNewRecord("`Patient`",6,"(`First Name`,`Last Name`,`Phone Number`,`Adress`,`Date of birth`,`Email`)",value)

def RemovePatient(id):
    RemoveRecord("`Patient`","`Patient ID`",id)

def UpdatePatient(id,valuetochange,newvalue):
    UpdateRecord("`Patient`","`Patient ID`",id,valuetochange,newvalue)

def ListPatients():
    return ListTable("`Patient`")

#UpdatePatient(1,"`First Name`","'kem'")   

#AddNewPatient(("omar","unal",454,"foyoyo sok sok","21 mart 2003","omyuny@gmaik.com"))
    
# ---------------------Doctor
    
def AddNewDoctor(value):
    AddNewRecord("`Doctor`",4,"(`First Name`,`Last Name`,`Department`,`Specialty`)",value)

def RemovePatient(id):
    RemoveRecord("`Doctor`","Doctor ID",id)

def UpdatePatient(id,valuetochange,newvalue):
    UpdateRecord("`Doctor`","Doctor ID",id,valuetochange,newvalue)

def ListDoctors():   
    return ListTable("`Doctor`")

#AddNewDoctor(("omar","vdf","game department","game design"))

#db.mydb.close()