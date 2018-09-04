import cgi, os


form = cgi.FieldStorage()
userid = form["userid"].value
password = form["password"].value
prenom = form["prenom"].value


open_file = open('data/' +pageId, 'w')
open_file.write(password)
open_file.close()

# os.rename('data/'+userid, 'data/'+title)

print("Location: index.py?id="+userid)
print("\n")
