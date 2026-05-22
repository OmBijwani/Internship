import sqlite3 
conn = sqlite3.connect("db1.db")

ins1 = """
INSERT INTO student(st_nm) 
VALUES("Om");
"""
ins2 = """
INSERT INTO faculty(f_nm) 
VALUES("Surbhi");
"""

conn.executescript(ins1) 
conn.executescript(ins2) 
conn.commit() 
conn.close() 