import sqlite3

conn = sqlite3.connect("pd.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE call
                      (
                          Crime_Id text primary key, Original_Crime_Type_Name text, Report_Date text,
                          Call_Date text, Offense_Date text, Call_Time text, Call_Date_Time text,
                          Disposition text, Address text, City text, State text, Agency_Id text, Address_Type text,
                          Common_Location text
                      )
               """)
