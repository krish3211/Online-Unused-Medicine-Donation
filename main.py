#!C:/python/python.exe
import mysql.connector
import cgi
def redir():
    redirectURL = "main.php"
    print('<html>')
    print('  <head>')
    print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
    print('  </head>')
    print('</html>')
print("Content-Type: text/html\n")
form = cgi.FieldStorage()

con = mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="user")
print(con)

fn = str(form.getvalue("username"))

ln = str(form.getvalue("password"))
cursor = con.cursor()
query = ("SELECT fname,lname FROM student WHERE fname='{}'AND lname='{}'".format(fn,ln))


cursor.execute(query)
a= cursor.fetchall()

if (fn,ln) in a :
    redir()
else:
    print("please re-login again")
    print("<button type='submit'><a href='http://localhost/Ngo/login.html'>submit</a></button>")

cursor.close()
con.close()