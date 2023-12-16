#from GUI import *
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:minecraft172@localhost/HospitalData")

"""insertStatement = sqlalchemy.insert("Patient").values(First_Name = "omyy",Last_Name="oi")

with engine.connect() as conn:
    conn.execute(insertStatement)
    conn.commit()"""

querry = "select * from Patient"

readdata = pd.read_sql(querry,engine)

print(readdata)