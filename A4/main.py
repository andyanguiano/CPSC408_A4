#Andy Anguiano
#CPSC408-01
#A4

#imports connection file
import connection

#gets information from user through console to run application
def runner():
    fileName = str(input("What would you like the .csv file to be named?(No extension): "))
    fileLength = int(input("How many records would you like to store in the database?: "))
    #runs correct functions to run program
    connection.exportData(connection.createData(fileName, fileLength))

    print("Successfully added " + str(fileLength) + " rows to the database.")

#runs application
if __name__ == '__main__':
    runner()
