import pymysql
import streamlit as st

st.set_page_config('HotelCoderFornia',None,'centered','expanded',
                   menu_items={
                    'About':'Your hotel reservation system built by the RoomReservers with Alison, Ylyas and Luna'})
# Establish a connection to the SQL Server database
conn = pymysql.connect(db='hotel_database', user='root', passwd='', host='localhost', port=3306)

st.title('Welcome to Room Reservers, Hotel CoderFornia')

#print connection establisment
'Connection at', conn



# Create a cursor object to interact with the database
cursor = conn.cursor()

Option1= st.selectbox(
    'What would you like to do?',
    ('Booking', 'View Records'))

#Do a booking or view a record
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
            cursor.execute('Describe Booking')
            results=cursor.fetchall()
            st.table(results)
        elif Option3 == 'View a record':
            st.header('View a record')
            Option4=st.number_input('Enter the **Booking ID** number',1,None,1)
            cursor.execute('SELECT * FROM booking WHERE Booking_ID=%s',(int(Option4)))
            results=cursor.fetchone()
            st.table(results)
            st.info(':exclamation: Results are displayed in the following order:')
            st.info('Booking ID, Customer ID, Hotel_ID, Arrival Date, Departure Date, Pax')

        
    elif Option2 == 'Customers':
        st.header(Option2)
        Option3= st.selectbox(
            'Which option would you like to run?',
            ('Describe a table', 'View a record'))
        
        if Option3 == 'Describe a table':
            st.header(Option3)
            cursor.execute('Describe Customers')
            results=cursor.fetchall()
            st.table(results)
        elif Option3 == 'View a record':
            st.header('View a record')
            Option4=st.number_input('Enter the **Customer ID** number',1,None,1)
            cursor.execute('SELECT * FROM customers WHERE ID=%s',(int(Option4)))
            results=cursor.fetchone()
            st.table(results)
            st.info(':exclamation: Results are displayed in the following order:')
            st.info('ID,Last Name, First Name, Passport Number, Passport Expiry, Date of birth, Phone no., Nationaility, Sex, Email, Credit Card')

        


    elif Option2 == 'Guest':
        st.header(Option2)
        Option3= st.selectbox(
            'Which option would you like to run?',
            ('Describe a table', 'View a record'))
        
        if Option3 == 'Describe a table':
            st.header(Option3)
            cursor.execute('Describe Guest')
            results=cursor.fetchall()
            st.table(results)
        elif Option3 == 'View a record':
            st.header('View a record')
            Option4= st.selectbox(
                'How would you like to sort by?',
                ('Guest ID', 'First Name and Last Name', 'Passport'))
            
            if Option4 == 'Guest ID':
                Option5= st.number_input('Enter the **Guest ID** number',1,None,1)
                cursor.execute('SELECT * FROM guest WHERE Guest_ID=%s',(int(Option5)))
                results=cursor.fetchone()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('Guest ID, Customer ID, Hotel ID, Booking ID, Guest First Name, Guest Last Name, Guest Passport, Additional Notes')
            if Option4 == 'First Name and Last Name':
                FirstName= st.text_input('Enter the first Name',str,255,'default',)
                LastName= st.text_input('Enter the last Name',str,255,'default')
                cursor.execute('SELECT * FROM guest WHERE Guest_F_Name =%s AND Guest_L_Name =%s',str(FirstName),str(LastName))
                results=cursor.fetchall()
                st.table()
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('Guest ID, Customer ID, Hotel ID, Booking ID, Guest First Name, Guest Last Name, Guest Passport, Additional Notes')
            
        
        
    elif Option2 == 'Room':
        st.header(Option2)
        Option3= st.selectbox(
            'Which option would you like to run?',
            ('Describe a table', 'View a record'))
        
        if Option3 == 'Describe a table':
            st.header(Option3)
            cursor.execute('Describe Room')
            results=cursor.fetchall()
            st.table(results)
        elif Option3 == 'View a record':
           st.header('View a record')
           Option4 = st.number_input('Enter the **Room ID** number',1,None,1)
           cursor.execute('SELECT * FROM room WHERE Hotel_ID=%s',(int(Option4)))
           results=cursor.fetchone()
           st.table(results)
           st.info(':exclamation: Results are displayed in the following order:')
           st.info('Hotel ID, Beds, Type of Bed, Price, Minibar included, Entertainment System, Bathtub, Notes')



# Close the cursor and connection
cursor.close()

conn.close()
