import sqlite3, csv

import log

conn = sqlite3.connect("pd.db")
cursor = conn.cursor()


@log.log
def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        cursor.execute("""insert into call (Crime_Id, Original_Crime_Type_Name, Report_Date, Call_Date, Offense_Date, 
                                            Call_Time, Call_Date_Time, Disposition, Address, City, State, Agency_Id, 
                                            Address_Type, Common_Location ) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?);""",
                       [
                           line["Crime Id"], line["Original Crime Type Name"], line['Report Date'], line['Call Date'],
                           line['Offense Date'], line['Call Time'], line['Call Date Time'], line['Disposition'],
                           line['Address'], line['City'], line['State'], line['Agency Id'], line['Address Type'],
                           line['Common Location']
                       ]
                       )
        conn.commit()


with open("police-department-calls-for-service.csv") as f_obj:
    csv_dict_reader(f_obj)
