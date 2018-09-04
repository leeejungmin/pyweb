import MySQLdb

mydb = MySQLdb.connect(
  host="localhost",
  user="root",
  passwd="111111",
  database="loginsystem"
)

#begin database
mycursor = mydb.cursor()
sql = "DROP TABLE user"
mycursor.execute(sql)
conn.commit()
#show all data
sql = "SELECT * FROM user"
for row in conn.execute(sql):
    print(row)
#insert data
# mycursor.excute("INSERT INTO example (language, Version, Skill) VALUES (?,?,?)",(lang, version, skill))
#
# conn.commit()
#
# db.close()
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")
