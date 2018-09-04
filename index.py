#!C:\Users\dlwjd\AppData\Local\Programs\Python\Python37\python.exe -u
print("Content-Type: text/html\n")
from watch import clock
import cgi, os


from tkinter import *
from time import strftime





form = cgi.FieldStorage()
if 'userid' in form:
    userid = form['userid'].value

    description = open('includes/data/'+userid, 'r').read()
else:
    userid = 'Welcome'
    description = 'Hello, web'

files = os.listdir('includes/data')
listStr=''
for title in files:
    listStr += '<a href="index.py?userid={userid}">{userid}</a><br><br>'.format(userid=title)

clk=new clock()
clk.root.mainloop()

print('''<!doctype html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    {listStr}
    <br>
    <a href="inscription.py">inscription</a>
    <form action="process_update.py" method="post">
        <input type="hidden" name="userid" value="">

        <p><textarea rows="4" name="description"
        placeholder="description">{description}</textarea></p>
        <p><input type="submit"></p>
    </form>
    <p id="checkk">JE suis Jungmin. J'etudie francais et programmation.c'est pour
    ca que j'ecris le francais ici , cette page.^^ </p>
    <h2>{userid}</h2>
    <p>{description}</p>
    <button type="button">clock</button>
    <script>document.getElementById("checkk").style.color="red"</script>
</body>
</html>
'''.format(userid=userid,description=description,listStr=listStr))
