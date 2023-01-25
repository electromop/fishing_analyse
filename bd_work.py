import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/user/Desktop/codes/python_codes/fishing_analyse/database/originial_html1.accdb;')
cursor = conn.cursor()
cursor.execute('select * from products')
   
for row in cursor.fetchall():
    print (row)