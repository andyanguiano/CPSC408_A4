#Andy Anguiano
#CPSC408-01
#A4

#import necessary files
import mysql.connector
import csv
from faker import Faker

#connect to database with my specific login information
db = mysql.connector.connect(
    host="34.94.182.22",
    user="aanguiano@chapman.edu",
    passwd="FooBar!@#$",
    database="aanguiano_db"
)

#takes file name and number of rows to create and creats fake rows and adds to .csv file
def createData(fileName, numRows):
    #adds extension and opens file to write
    fileName = fileName + ".csv"
    file = open(fileName, "w")
    add = csv.writer(file)

    #adds the title row of all variables in datasheet
    add.writerow(["partName", "partPrice", "cName", "cAddress", "cCity", "cState", "cZipCode", "cEmail", "quantity", "date", "type", "sName", "sPhone", "sState", "eName", "ePhone", "eDepartment"])

    #options for certain variables
    departments = ["Customer Service", "Manager", "Other"]
    types = ["Phone", "Store", "Email"]

    #uses faker to create the specified number of rows for the datasheet
    fake = Faker()
    for i in range(0, numRows):
        add.writerow([fake.word(), fake.random_int(0,1000), fake.name(), fake.street_name(), fake.city(), fake.state(), fake.zipcode(), fake.email(), fake.random_int(1,10000), fake.date(), types[fake.random_int(0,2)], fake.name(), fake.phone_number(), fake.state(), fake.name(), fake.phone_number(), departments[fake.random_int(0,2)]])

    #returns file name for use in exportData()
    return fileName

#seperates the datasheet values and puts them into the daabase
def exportData(fileName):
    #creates cursor to allow for sql queries
    mycursor = db.cursor()
    theFile = "./" + fileName

    #opens the specified file to use information
    with open(theFile) as information:
        #uses dictreader to accuratly access the correct variables
        reader = csv.DictReader(information)

        #goes through all the data seperates each line
        for line in reader:
            #adds correct info into Parts table
            mycursor.execute("INSERT INTO Parts(pName, pPrice) VALUES(%s,%s)", (line['partName'], line['partPrice']))
            db.commit()
            #adds correct info into Customer table
            mycursor.execute("INSERT INTO Customer(cName, cAddress, cCity, cState, cZipCode, cEmail) VALUES(%s,%s,%s,%s,%s,%s)", (line["cName"], line["cAddress"], line["cCity"], line["cState"], line["cZipCode"], line["cEmail"]))
            db.commit()
            #adds correct info into Invoice table
            mycursor.execute("INSERT INTO Invoice(part, quantity, date, type, customer, employee) VALUES(%s,%s,%s,%s,%s,%s)", (line["partName"], line["quantity"], line["date"], line["type"], line["cName"], line["eName"]))
            db.commit()
            #adds correct info into Supplier table
            mycursor.execute("INSERT INTO Supplier(sName, sPhone, sState) VALUES(%s,%s,%s)", (line["sName"], line["sPhone"], line["sState"]))
            db.commit()
            #adds correct info into Employee table
            mycursor.execute("INSERT INTO Employee(eName, ePhone, department) VALUES(%s,%s,%s)", (line["eName"], line["ePhone"], line["eDepartment"]))
            db.commit()