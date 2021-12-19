#!C:/python/python.exe
import mysql.connector
import cgi
print("Content-Type: text/html\n")
form = cgi.FieldStorage()

con = mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="user")
print(con)

mn = str(form.getvalue("MedicineName"))
mc = str(form.getvalue("MedicineCount"))
ed = str(form.getvalue("ExpiryDate"))
pn = str(form.getvalue("PhoneNunmber"))

cursor = con.cursor()
insert = "INSERT INTO `data`(`PersonName`, `city/village`, `MedicineName`, `MedicineUses`, `MedicineCount`, `ExpiryDate`, `PhoneNo`) VALUES ('abbas','chennai',%s,'-',%s,%s,%s)"


cursor.execute(insert,(mn,mc,ed,pn))
con.commit()
redirectURL = "thank.html"
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>') 

cursor.close()
con.close()


