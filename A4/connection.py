import mysql.connector

def theConnection():
    db = mysql.connector.connect(
        host="34.94.182.22",
        user="aanguiano@chapman.edu",
        passwd="FooBar!@#$",
        database="aanguiano_db"
    )

    mycursor = db.cursor()
    mycursor.execute("CREATE TABLE Student")
    data = mycursor.fetchall()

    print(data)


theConnection()