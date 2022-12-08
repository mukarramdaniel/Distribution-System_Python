import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  password="Rosepetal514@",
  database="dbarm"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Employee (empID) VALUES (1)"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
