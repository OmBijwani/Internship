import sqlite3

conn = sqlite3.connect("db1.db")

sql = """ 
Create table student( 
st_id INTEGER PRIMARY KEY AUTOINCREMENT, 
st_nm VARCHAR(50)  
); 
             
Create table faculty( 
f_id INTEGER PRIMARY KEY AUTOINCREMENT, 
f_nm VARCHAR(50) 
);

"""
conn.executescript(sql)
conn.close()