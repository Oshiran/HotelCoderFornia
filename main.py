import datetime as dt
import pymysql
import streamlit as st

st.set_page_config('HotelCoderFornia',None,'wide','auto',
                   menu_items={'About':'Your hotel reservation system built by the RoomReservers'})

# Establish a connection to the SQL Server database
conn = pymysql.connect(db='hotel_database', user='root', passwd='', host='localhost', port=3306)

st.title('Welcome to Room Reservers, Hotel CoderFornia')


# Create a cursor object to interact with the database
cursor = conn.cursor()

Option1= st.selectbox(
    'What would you like to do?',
    ('Booking', 'View Records'))

#Do a booking or view a record
if Option1 == 'Booking':
    st.header(Option1)
    
    st.subheader('New Record')
    Option2=st.selectbox('Which new would you like to make',('Booking','Customer','Guest',))

    #New Booking record
    if Option2 == "Booking":
        st.subheader('New Booking Record')
        with st.form('21',True):
            Var2=st.number_input('Enter Customer ID',1,step=1,key=1)
            Var3=st.number_input('Enter Room ID',1,step=1,key=2)
            Var4=st.date_input('Enter Arrival Date',dt.datetime.today(),dt.datetime.today(),key=3)
            Var5=st.date_input('Enter Departure Date',dt.datetime.today(),dt.datetime.today(),key=4)
            Var6=st.number_input('Enter Pax',1,value=1,key=5)
            submit=st.form_submit_button('Submit')
            if submit == True:
                cursor.execute('INSERT INTO booking(ID, Hotel_ID, Arrival_Date, Departure_Date, Pax) VALUES (%s, %s, %s, %s, %s)',(Var2,Var3,Var4,Var5,Var6))
                conn.commit()
                st.write('Record entered')
                st.info('Listed below are information you have entered')
                st.write(Var2,Var3,Var4,Var5,Var6)
                st.write('Record entered')
                st.balloons()
    #New Customer Record
    if Option2 == "Customer":
        st.subheader('New Customer Record')
        with st.form('10',True):
            Var2 = st.text_input('Enter First Name',key=6)
            Var3 = st.text_input('Enter Last Name',key=7)
            Var4 =st.text_input('Enter Passport number',max_chars=15,key=8)
            Var5 =st.date_input('Enter Passport Expiration',min_value=dt.datetime.today(),key=9)
            Var6 =st.date_input('Enter Date of birth',dt.datetime.today(),dt.date(1850,1,1),dt.datetime.today(),10)
            Var7 =st.text_input('Enter phone number',max_chars=15,key=11)
            Var8 =st.text_input('Enter Nationality',key=12)
            Var9 =st.radio('Enter Gender',options=['Male','Female'],horizontal=True,key=13)
            Var10 =st.text_input('Enter e-mail address','',key=14)
            Var11 =st.text_input('Enter credit card',type='password',key=15)
            submit=st.form_submit_button('Submit')
            if submit == True:
                cursor.execute('INSERT INTO customers(L_name, F_Name, Passport_No, Passport_Exp, DOB, Phone_no, Nationality, Sex, Email, Credit_Card) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11))
                conn.commit()
                st.write('Record entered')
                st.info('Listed below are information you have entered')
                st.write(Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11)
                st.balloons()
    #New Guest Record
    if Option2 == "Guest":
        st.subheader('New Guest Record')
        with st.form('28',True):
            Var2=st.number_input('Enter Guest ID',1,step=1,key=16)
            Var3=st.number_input('Enter ID',1,step=1,key=17)
            Var4=st.number_input('Enter Hotel ID',1,step=1,key=64)
            Var5=st.number_input('Enter Booking ID',1,step=1,key=18)
            Var6=st.text_input('Enter Guest First Name',key=19)
            Var7=st.text_input('Enter Guest Last Name',key=20)
            Var8=st.text_input('Enter Guest Passport',max_chars=15,key=21)
            Var9=st.text_input('Enter any additional notes', key=22)
            submit=st.form_submit_button('Submit')
            if submit == True:
                cursor.execute('INSERT INTO guest(Guest_ID, ID, Hotel_ID, Booking_ID, Guest_F_Name, Guest_L_Name, Guest_Passport, G_notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',(Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9))
                conn.commit()
                st.write('Record entered')
                st.info('Listed below are information you have entered')
                st.write(Var2,Var3,Var4,Var5,Var6,Var7,Var8)
                st.balloons()
                st.write('Record entered')
                st.balloons()
                

    #View Records
elif Option1 == 'View Records':
    st.header(Option1)
    
    #Seperate tabs for each table for ease
    tab1, tab2, tab3, tab4 = st.tabs([':blue[**Booking**]', ':blue[**Customers**]', ':blue[**Guest**]', ':blue[**Room**]'])

    #View Booking
    with tab1:
        st.subheader('Table: Booking')
        Option2= st.selectbox(
            'What would you like to do?',
            ('View a record','Describe a table')) 
        
        if Option2 == 'Describe a table':
            st.subheader(Option2)
            cursor.execute('Describe Booking')
            results=cursor.fetchall()
            st.table(results)
        elif Option2 == 'View a record':
            st.subheader('View a record')
            Option3=st.number_input('Enter the **Booking ID** number',1,None,1,1,key=23) 
            cursor.execute('SELECT * FROM booking WHERE Booking_ID=%s',(int(Option3)))
            results=cursor.fetchone()
            st.table(results)
            st.info(':exclamation: Results are displayed in the following order:')
            st.info('Booking ID, Customer ID, Hotel_ID, Arrival Date, Departure Date, Pax')

        st.divider()
        st.subheader('Would you like to ammend the following record?')
        Option3=st.radio('Select',['No','Yes'], horizontal=True,key=24)
        if Option3 == 'Yes':
            var=st.number_input('What was the original Booking ID?',1,value=1,step=25)
            with st.form('36',True):
                Var2=st.number_input('Enter Customer ID',1,step=1,key=26)
                Var3=st.number_input('Enter Room ID',1,step=1,key=27)
                Var4=st.date_input('Enter Arrival Date',dt.datetime.today(),dt.datetime.today(),key=28)
                Var5=st.date_input('Enter Departure Date',dt.datetime.today(),dt.datetime.today(),key=29)
                Var6=st.number_input('Enter Pax',1,value=1,key=30)
                submit=st.form_submit_button('Submit')
            if submit == True:
                cursor.execute('UPDATE booking SET ID=%s, Hotel_ID=%s, Arrival_Date=%s, Departure_Date=%s, Pax=%s WHERE Booking_ID=%s',(Var2,Var3,Var4,Var5,Var6,var))
                conn.commit()
                st.write('Record Updated')
                st.info('Listed below are information you have entered')
                st.write(Var2,Var3,Var4,Var5,Var6,var)
                st.balloons()
        
        if Option3 == 'No':
            st.subheader(' Acknowledged :ok_hand: :ok_hand: :ok_hand:')
            

 
    #View Customers
    with tab2:
        st.subheader('Table: Customers')

        Option2= st.selectbox(
            'Which option would you like to run?',
            ('View a record','Describe a table'),0,str,key=31) 
        
        if Option2 == 'Describe a table':
            st.subheader(Option2)
            cursor.execute('Describe Customers')
            results=cursor.fetchall()
            st.table(results)
        
        elif Option2 == 'View a record':
            st.subheader(Option2)
            Option3=st.selectbox('How would you like to sort by?',('ID','First and Last Name','Passport no.'))
            
            if Option3 == 'ID':
                CustomerID=int(st.number_input('Enter the **Customer ID** number',1,None,1,1,key=32))
                cursor.execute('SELECT * FROM customers WHERE ID=%s',(CustomerID))
                results=cursor.fetchone()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('ID,Last Name, First Name, Passport Number, Passport Expiry, Date of birth, Phone no., Nationaility, Sex, Email, Credit Card')
            
            elif Option3 == 'First and Last Name':
                FirstName= str(st.text_input('Enter the first Name',key=33))
                LastName= str(st.text_input('Enter the last Name',key=34))
                cursor.execute('SELECT * FROM customers WHERE F_Name =%s AND L_Name =%s',(FirstName, LastName))
                results=cursor.fetchall()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('ID,Last Name, First Name, Passport Number, Passport Expiry, Date of birth, Phone no., Nationaility, Sex, Email, Credit Card')
            
            elif Option3 == 'Passport no.':
                Passport=Passport= str(st.text_input('Enter the Passport/IC number',max_chars=15,key=35))
                cursor.execute('SELECT * FROM customers WHERE Passport_no=%s',(Passport))
                results=cursor.fetchall()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('ID,Last Name, First Name, Passport Number, Passport Expiry, Date of birth, Phone no., Nationaility, Sex, Email, Credit Card')
        
            st.divider()
            st.subheader('Would you like to ammend the following record?')
            Option3=st.radio('Select',['No','Yes'], horizontal=True,key=62)
            if Option3 == 'Yes':
                var=st.number_input('What was the original ID?',1,value=1,step=1)
                with st.form('52',True):
                    Var2 = st.text_input('Enter First Name',key=37)
                    Var3 = st.text_input('Enter Last Name',key=38)
                    Var4 =st.text_input('Enter Passport number',max_chars=15,key=39)
                    Var5 =st.date_input('Enter Passport Expiration',min_value=dt.datetime.today(),key=40)
                    Var6 =st.date_input('Enter Date of birth',dt.datetime.today(),dt.date(1850,1,1),dt.datetime.today(),41)
                    Var7 =st.text_input('Enter phone number',max_chars=15,key=42)
                    Var8 =st.text_input('Enter Nationality',key=43)
                    Var9 =st.radio('Enter Gender',options=['Male','Female'],horizontal=True,key=44)
                    Var10 =st.text_input('Enter e-mail address','',key=45)
                    Var11 =st.text_input('Enter credit card',type='password',key=46)
                    submit=st.form_submit_button('Submit')
                if submit == True:
                    cursor.execute('UPDATE customers SET F_Name=%s, L_Name=%s, Passport_No=%s, Passport_Exp=%s, DOB=%s, Phone_no=%s, Nationality=%s, Sex=%s, Email=%s, Credit_Card=%s WHERE ID=%s',(Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11,var))
                    conn.commit()
                    st.write('Record Updated')
                    st.info('Listed below are information you have entered')
                    st.write(var,Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11)
                    st.balloons()
            
            if Option3 == 'No':
                st.subheader(' Acknowledged :ok_hand: :ok_hand: :ok_hand:')

    #View Guest
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
                Option4= st.number_input('Enter the **Guest ID** number',1,None,1,1,key=60)
                cursor.execute('SELECT * FROM guest WHERE Guest_ID=%s',(int(Option4)))
                results=cursor.fetchone()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('Guest ID, Customer ID, Hotel ID, Booking ID, Guest First Name, Guest Last Name, Guest Passport, Additional Notes')
            if Option3 == 'First Name and Last Name':
                FirstName= str(st.text_input('Enter the first Name','',255,43))
                LastName= str(st.text_input('Enter the last Name','',255,44))
                cursor.execute('SELECT * FROM guest WHERE Guest_F_Name =%s AND Guest_L_Name =%s',(FirstName, LastName))
                results=cursor.fetchall()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('Guest ID, Customer ID, Hotel ID, Booking ID, Guest First Name, Guest Last Name, Guest Passport, Additional Notes')
            if Option3 == 'Passport':
                Passport= str(st.text_input('Enter the Passport/IC number','',255,45))
                cursor.execute('SELECT * FROM guest WHERE Guest_Passport=%s',(Passport))
                results=cursor.fetchall()
                st.table(results)
                st.info(':exclamation: Results are displayed in the following order:')
                st.info('Guest ID, Customer ID, Hotel ID, Booking ID, Guest First Name, Guest Last Name, Guest Passport, Additional Notes')
            
            st.divider()
            st.subheader('Would you like to ammend the following record?')
            Option3=st.radio('Select',['No','Yes'], horizontal=True,key=61)
            if Option3 == 'Yes':
                var=st.number_input('What was the original Guest ID?',1,value=1,step=1)
                with st.form('63',True):
                    Var2=st.number_input('Enter Customer ID',1,step=1,key=16)
                    Var3=st.number_input('Enter Room ID',1,step=1,key=17)
                    Var4=st.number_input('Enter Booking ID',1,step=1,key=18)
                    Var5=st.text_input('Enter Guest First Name',key=19)
                    Var6=st.text_input('Enter Guest Last Name',key=20)
                    Var7=st.text_input('Enter Guest Passport',max_chars=15,key=21)
                    Var8=st.text_input('Enter any additional notes', key=22)
                    submit=st.form_submit_button('Submit')
                if submit == True:
                    cursor.execute('UPDATE guest SET ID=%s, Hotel_ID=%s, Booking_ID=%s, Guest_F_Name=%s, Guest_L_Name=%s, Guest_Passport=%s, G_notes=%s WHERE Guest_ID=%s',(Var2,Var3,Var4,Var5,Var6,Var7,Var8,var))
                    conn.commit()
                    st.write('Record Updated')
                    st.info('Listed below are information you have entered')
                    st.write(Var2,Var3,Var4,Var5,Var6,Var7,Var8,var)
                    st.balloons()
        
        if Option3 == 'No':
            st.subheader(' Acknowledged :ok_hand: :ok_hand: :ok_hand:')
    
    #View Room
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
    st.subheader(':violet[You are currently are in:]')
    st.subheader(Option1)
    st.warning('🚨Always make sure all fields are field or the system will crash🚨 Refresh the page should you run into an error')

# Close the cursor and connection
cursor.close()

conn.close()
