import datetime as dt
import pymysql
import streamlit as st

st.set_page_config('HotelCoderFornia',None,'centered','expanded',
                   menu_items={'About':'Your hotel reservation system built by the RoomReservers'})
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
    tab5,tab6 = st.tabs([':blue[**New record**]', ':blue[**Update Records**]'])
    
    with tab5:
        Option2=st.selectbox('Which New would you like to make',('Booking','Customer','Guest',))

        if Option2 == "Booking":
            st.subheader('New Booking Record')

        if Option2 == "Customer":
            st.subheader('New Customer Record')
            with st.form('10',True):
                Var2 = st.text_input('Enter First Name','',255,11)
                Var3 = st.text_input('Enter Last Name','',255,12)
                Var4 =st.text_input('Enter Passport number','',15,13)
                Var5 =st.date_input('Enter Passport Expiration',None,None,None,14)
                Var6 =st.date_input('Enter Date of birth',dt.datetime.today(),dt.date(1850,1,1),dt.datetime.today(),15)
                Var7 =st.text_input('Enter phone number','',15,16)
                Var8 =st.text_input('Enter Nationality','',255,17)
                Var9 =st.radio('Enter Gender',options=['Male','Female'],horizontal=True,key=18)
                Var10 =st.text_input('Enter e-mail address','',255,19)
                Var11 =st.text_input('Enter credit card',type='password')
                submit=st.form_submit_button('Submit')
                if submit == True:
                    # cursor.execute('INSERT INTO customers(L_name,F_Name,Passport_No,Passport_Exp,DOB,Phone_no,Nationality,Sex,Email,Credit_Card) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)',(Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11))
                    # conn.commit()
                    st.write('Record entered')
                
        if Option2 == "Guest":
            st.subheader('New Guest Record')
    
    with tab6:
        st.subheader('Update records')
     
elif Option1 == 'View Records':
    st.header(Option1)
    
    tab1, tab2, tab3, tab4 = st.tabs([':blue[**Booking**]', ':blue[**Customers**]', ':blue[**Guest**]', ':blue[**Room**]'])

    with tab1:
        st.subheader('Table: Booking')
        Option2= st.selectbox(
            'What would you like to do?',
            ('View a record','Describe a table'),0,str,1)
        
        if Option2 == 'Describe a table':
            st.subheader(Option2)
            cursor.execute('Describe Booking')
            results=cursor.fetchall()
            st.table(results)
        elif Option2 == 'View a record':
            st.subheader('View a record')
            Option3=st.number_input('Enter the **Booking ID** number',1,None,1)
            cursor.execute('SELECT * FROM booking WHERE Booking_ID=%s',(int(Option3)))
            results=cursor.fetchone()
            st.table(results)
            st.info(':exclamation: Results are displayed in the following order:')
            st.info('Booking ID, Customer ID, Hotel_ID, Arrival Date, Departure Date, Pax')
    
    with tab2:
        st.subheader('Table: Customers')

        Option2= st.selectbox(
            'Which option would you like to run?',
            ('View a record','Describe a table'),0,str,2)
        
        if Option2 == 'Describe a table':
            st.subheader(Option2)
            cursor.execute('Describe Customers')
            results=cursor.fetchall()
            st.table(results)
        
        elif Option2 == 'View a record':
            st.subheader(Option2)
            Option3=st.selectbox('How would you like to sort by?',
                                 ('ID','First and Last Name','Passport no.'))
            
            if Option3 == 'ID':
                CustomerID=int(st.number_input('Enter the **Customer ID** number',1,None,1))
                cursor.execute('SELECT * FROM customers WHERE ID=%s',(CustomerID))
                results=cursor.fetchone()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('ID,Last Name, First Name, Passport Number, Passport Expiry, Date of birth, Phone no., Nationaility, Sex, Email, Credit Card')
            
            elif Option3 == 'First and Last Name':
                FirstName= str(st.text_input('Enter the first Name','',255,8))
                LastName= str(st.text_input('Enter the last Name','',255,9))
                cursor.execute('SELECT * FROM customers WHERE F_Name =%s AND L_Name =%s',(FirstName, LastName))
                results=cursor.fetchall()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('ID,Last Name, First Name, Passport Number, Passport Expiry, Date of birth, Phone no., Nationaility, Sex, Email, Credit Card')
            
            elif Option3 == 'Passport no.':
                Passport=Passport= str(st.text_input('Enter the Passport/IC number','',255,9))
                cursor.execute('SELECT * FROM customers WHERE Passport_no=%s',(Passport))
                results=cursor.fetchall()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('ID,Last Name, First Name, Passport Number, Passport Expiry, Date of birth, Phone no., Nationaility, Sex, Email, Credit Card')

    
    with tab3:
        st.subheader('Table: Guest')

        Option2= st.selectbox(
            'Which option would you like to run?',
            ('View a record','Describe a table'),0,str,3)
        
        if Option2 == 'Describe a table':
            st.subheader(Option2)
            cursor.execute('Describe Guest')
            results=cursor.fetchall()
            st.table(results)

        elif Option2 == 'View a record':
            st.subheader(Option2)
            Option3= st.selectbox(
                'How would you like to sort by?',
                ('Guest ID', 'First Name and Last Name', 'Passport'))
            
            if Option3 == 'Guest ID':
                Option4= st.number_input('Enter the **Guest ID** number',1,None,1)
                cursor.execute('SELECT * FROM guest WHERE Guest_ID=%s',(int(Option4)))
                results=cursor.fetchone()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('Guest ID, Customer ID, Hotel ID, Booking ID, Guest First Name, Guest Last Name, Guest Passport, Additional Notes')
            if Option3 == 'First Name and Last Name':
                FirstName= str(st.text_input('Enter the first Name','',255,6))
                LastName= str(st.text_input('Enter the last Name','',255,7))
                cursor.execute('SELECT * FROM guest WHERE Guest_F_Name =%s AND Guest_L_Name =%s',(FirstName, LastName))
                results=cursor.fetchall()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('Guest ID, Customer ID, Hotel ID, Booking ID, Guest First Name, Guest Last Name, Guest Passport, Additional Notes')
            if Option3 == 'Passport':
                Passport= str(st.text_input('Enter the Passport/IC number','',255,8))
                cursor.execute('SELECT * FROM guest WHERE Guest_Passport=%s',(Passport))
                results=cursor.fetchall()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('Guest ID, Customer ID, Hotel ID, Booking ID, Guest First Name, Guest Last Name, Guest Passport, Additional Notes')

    with tab4:
        st.subheader('Table: Room')
        Option2= st.selectbox(
            'Which option would you like to run?',
            ('View a record', 'Describe a table'),0,str,4)
        
        if Option2 == 'Describe a table':
            st.subheader(Option2)
            cursor.execute('Describe Room')
            results=cursor.fetchall()
            st.table(results)
        elif Option2 == 'View a record':
           st.subheader(Option2)
           Option3 = st.number_input('Enter the **Room ID** number',1,None,1)
           cursor.execute('SELECT * FROM room WHERE Hotel_ID=%s',(int(Option3)))
           results=cursor.fetchone()
           st.table(results)
           st.info(':exclamation: Results are displayed in the following order:')
           st.info('Hotel ID, Beds, Type of Bed, Price, Minibar included, Entertainment System, Bathtub, Notes')

with st.sidebar:
    st.title('Welcome to HotelCoderFornia')
    st.caption('Made by the RoomReservers!')
    st.header(':violet[You are currently are in:]')
    st.subheader(Option1)

# Close the cursor and connection
cursor.close()

conn.close()
