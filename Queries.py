# All queries up for testing can be found here

import pymysql

# Establish a connection to the SQL Server database
conn = pymysql.connect(db='hotel_database', user='root', passwd='', host='localhost', port=3306)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define a query and then followed by execution
def show_tables ():
    cursor.execute('show tables')
    # Fetch the results of the query
    results = cursor.fetchall()
    # Print the results
    for row in results:
        print(row)
show_tables()

#Describe table and return
TableName = input("Insert a table name from the follwing(booking,customers,guest,room):", )
def Describe (TableName):
    cursor.execute("Describe Customers")
    results = cursor.fetchall()
    for row in results:
        print(row)
Describe(TableName)



# Close the cursor and connection
cursor.close()

print(conn)
conn.close()
