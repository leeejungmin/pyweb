#!C:\Users\dlwjd\AppData\Local\Programs\Python\Python37\python.exe -u
print("Content-Type: text/html\n")


import cgi, os

form = cgi.FieldStorage()
# if 'id' in form:
    # pageId =form["id"].value
    # description = open('includes/'+pageId,'r').read()
    # description = description.replace('<', '&lt;')
    # description = description.replace('>', '&gt;')

    # update_link = '<a href="update.py?id={}">update</a>'.format(pageId)

content ='''

    <form id="inscrip" action="includes/process_creat.py" method="POST">
        <div>
          <p2>Userid</p2>
        </div>
        <div>
          <input id="userid" type="text" name="userid" placeholder="Entrez votre id" />
        </div>
        <div >
          <p2>Password</p2>
        </div>
        <div>
          <input ty pe="text" name="password" placeholder="Entrez votre password" />
        </div>
        <div >
          <p2>Prenom</p2>
        </div>
        <div>
          <input id="name" type="text" name="prenom" placeholder="Entrez votre prenom" />
        </div>
        <div >
          <p2>Nom</p2>
        </div>
        <div>
          <input type="text" name="nom" placeholder="Entrez votre nom..." />
        </div>
        <div >
          <p2>Age</p2>
        </div>
        <div>
          <input id="agee" type="number" name="age" placeholder="Entrez votre age" />
        </div>
        <div>
          <p2>civilite</p2>
        </div>
        <div>
          <label  >Madame
        <input  type="radio" name="radio" value="Madame" >
        <span ></span>
      </label>
      <label class="container" >Monsier
        <input type="radio" name="radio"  value="Monsier">
        <span  ></span>
      </label>
        <div >
          <p2>E-mail</p2>
        </div>
        <div>
          <input type="text" name="email" placeholder="Entrez votre e-mail..." />
        </div>
        <div id=buttonlogin>
          <button id='valid' type="submit" name="submit" >Valider</button>
        </div>
      </form>
    '''

# else:
# pageId='Welcome'
#
# print(pageId)

print('''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>WEB1 - Welcome</title>
    <link rel="stylesheet" type="text/css" href="includes/style.css" />
  </head>

  <body>

    <h1><a href="index.py">Inscription</a></h1>
    <div>
     {content}
     </div>

  </body>
</html>
'''.format(content=content))
