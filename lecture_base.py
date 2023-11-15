import sqlite3

con = sqlite3.connect('ma_base.db')
cur = con.cursor()
req = "select*from tracker"
result = cur.execute(req)
for row in result :
    print(row)