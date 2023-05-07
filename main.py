import pymysql
import streamlit as st


# Establish a connection to the SQL Server database
conn = pymysql.connect(db='hotel_database', user='root', passwd='', host='localhost', port=3306)

st.title('Welcome to Room Reservers, Hotel CoderFornia')

#print connection establisment
'Connection at', conn
st.balloons()
st.snow()


# Create a cursor object to interact with the database
cursor = conn.cursor()

Option1= st.selectbox(
    'What would you like to do?',
    ('Booking', 'View Records'))

#Pick between doing a booking or view a record
if Option1 == 'Booking':
    st.header(Option1)
     
elif Option1 == 'View Records':
    st.header(Option1)

    #Pick which table to retrive from
    Option2 = st.selectbox(
        'Which table would you like to view?',
        ('Booking','Customers','Guest','Room'))
    
    if Option2 == 'Booking':
        st.header(Option2)
         
        Option3= st.selectbox(
            'Which option would you like to run',
            ('Describe a table', 'View a record'))
        if Option3 == 'Describe a table':
            st.header(Option3)
        
        
    elif Option2 == 'Customers':
        st.header(Option2)
        Option3= st.selectbox(
            'Which option would you like to run',
            ('Describe a table', 'View a record'))
        if Option3 == 'Describe a table':
            st.header(Option3)
            cursor.execute('Describe Customers')
            results=cursor.fetchall()
            st.table(results)
         
    elif Option2 == 'Guest':
        st.header(Option2)
        
    elif Option2 == 'Room':
        st.header(Option2)
        



# Close the cursor and connection
cursor.close()

conn.close()
