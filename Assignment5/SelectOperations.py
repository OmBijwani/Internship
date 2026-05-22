import sqlite3 
conn = sqlite3.connect("db1.db") 
data= conn.execute("select * from student order by st_nm DESC limit 2") 
for m in data: 
    print(m) 

conn.close() 