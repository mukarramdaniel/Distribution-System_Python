import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  password="Rosepetal514@",
  database="dbarm"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT userID,password,userName,name,age,contactNum,Email,Cnic,bankAccount,resetToken  FROM manager")

myresult = mycursor.fetchall()

for x in :
  print(myresult)