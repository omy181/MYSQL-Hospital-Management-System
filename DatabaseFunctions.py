#from GUI import *
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

# Custom Functions

def AddNewPatient(value):
    AddNewRecord("`Patient`",6,"(`First Name`,`Last Name`,`Phone Number`,`Adress`,`Date of birth`,`Email`)",value)

def RemovePatient(id):
    RemoveRecord("`Patient`","`Patient ID`",id)

def UpdatePatient(id,valuetochange,newvalue):
    UpdateRecord("`Patient`","`Patient ID`",id,valuetochange,newvalue)

    

AddNewPatient(("omar","unal",454,"foyoyo sok sok","21 mart 2003","omyuny@gmaik.com"))

db.mydb.close()