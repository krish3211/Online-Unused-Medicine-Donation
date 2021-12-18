#!C:/python/python.exe
import mysql.connector
import cgi
def redir():
    redirectURL = "main.html"
    print('<html>')
    print('  <head>')
    print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
    print('  </head>')
    print('</html>')
print("Content-Type: text/html\n")
form = cgi.FieldStorage()

con = mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="user")
print(con)

ser = str(form.getvalue("search"))


cursor = con.cursor()
query = ("SELECT * FROM data WHERE MedicineName='{}'".format(ser))


cursor.execute(query)
a= cursor.fetchall()
for i in a:
    print(a)


cursor.close()
con.close()