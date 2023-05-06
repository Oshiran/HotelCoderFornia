import pymysql

# Establish a connection to the SQL Server database
conn = pymysql.connect(db='hotel_database', user='root', passwd='', host='localhost', port=3306)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM your_table')

# Fetch the results of the query
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()

print(conn)
conn.close()
