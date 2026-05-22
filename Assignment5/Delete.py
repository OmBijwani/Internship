import sqlite3 
conn = sqlite3.connect("db1.db") 
data= conn.execute("select * from student order by st_nm DESC") 
for m in data: 
    print(m)

delete_id = input("id to delete: ") 
conn.execute("delete from student where st_id =" +delete_id) 
conn.commit() 

data1 = conn.execute("select * from student order by st_nm DESC") 
for m in data1: 
    print(m)

conn.close() 