#!C:/python/python.exe
from typing import Counter
import mysql.connector
import cgi
print("Content-Type: text/html\n")
form = cgi.FieldStorage()

con = mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="user")
print(con)

name = str(form.getvalue("username"))
phoneno = str(form.getvalue("phoneno"))
Country = str(form.getvalue("country"))
state = str(form.getvalue("state"))
city = str(form.getvalue("city"))
pin = str(form.getvalue("pin"))
password = str(form.getvalue("password"))

cursor = con.cursor()
insert = "INSERT INTO `login`(`username`, `password`, `phoneno`, `pin`, `country`, `city`, `state`) VALUES (%s,%s,%s,%s,%s,%s,%s)"


cursor.execute(insert,(name,password,phoneno,pin,Counter,city,state))
con.commit()
print(cursor.rowcount)


cursor.close()
con.close()
print("<h1>sdasahafi</h1>")

