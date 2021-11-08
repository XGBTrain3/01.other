import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="demo",
  password="Demo",
  database="mydatabase3"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers1_2 (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")