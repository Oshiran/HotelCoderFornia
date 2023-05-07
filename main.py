import pymysql
import streamlit as st

# Establish a connection to the SQL Server database
conn = pymysql.connect(db='hotel_database', user='root', passwd='', host='localhost', port=3306)

st.title('Welcome to Room Reservers, Hotel CoderFornia')

#print connection establisment
'Connection at', conn
st.balloons()

# Create a cursor object to interact with the database
cursor = conn.cursor()

Option1= st.selectbox(
    'What would you like to do?',
    ('Booking', 'View Records'))

if Option1 == 'Booking':
    'You picked', Option1
elif Option1 == 'View Records':
    'You picked', Option1
    Option2 = st.selectbox(
        'Which table would you like to view?',
        ('Booking','Customers','Guest','Room'))
    if Option2 == 'Booking':
        'You picked', Option2
    elif Option2 == 'Customers':
        'You picked', Option2
    elif Option2 == 'Guest':
        'You picked', Option2
    elif Option2 == 'Room':
        'You picked', Option2


# Close the cursor and connection
cursor.close()

conn.close()
