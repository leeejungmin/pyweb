#!C:\Users\dlwjd\AppData\Local\Programs\Python\Python37\python.exe -u


import cgi


form = cgi.FieldStorage()
userid = form['userid'].value
password = form["password"].value

open_file = open('data/' +userid, 'w')
open_file.write(password)

print("Location: ../index.py?id="+userid)
print("\n")
