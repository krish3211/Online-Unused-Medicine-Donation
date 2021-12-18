#!C:/python/python.exe
import mysql.connector
import cgi
import requests as req
import webbrowser

def redir():
    return webbrowser.open('dashboard.html', new=2)
    '''redirectURL = "dashboard.html"
    print('<html>')
    print('  <head>')
    print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
    print('  </head>')
    print('</html>')'''

print("Content-Type: text/html\n")
form = cgi.FieldStorage()

con = mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="user")
print(con)

fn = str(form.getvalue("fname"))

ln = str(form.getvalue("lname"))
cursor = con.cursor()
query = ("SELECT fname,lname FROM student WHERE fname='{}'AND lname='{}'".format(fn,ln))


cursor.execute(query)
a= cursor.fetchall()

if (fn,ln) in a :
    redir()
else:
    print("please re-login again")
    print("<button type='submit'><a href='http://localhost/login/login.html'>submit</a></button>")

cursor.close()
con.close()
