import sqlite3 
conn = sqlite3.connect("db1.db") 
data = conn.execute("select * from student order by st_nm DESC") 
for m in data: 
    print(m) 

conn.execute("update student set st_nm = 'Nikhil' where st_id=1") 
conn.commit()

data1 = conn.execute("select * from student order by st_nm DESC") 
for m in data1: 
    print(m) 

conn.close()