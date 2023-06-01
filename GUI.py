import streamlit as st
import datetime as dt
import PYSQLexec as Pye
import functions as f

#Preferences for Streamlit before running the rest of the elements
def Setup():
    st.set_page_config('HotelCoderFornia',None,'wide','auto', menu_items={'About':'Your hotel reservation system built by the RoomReservers'})

#Sidebar elements
def sidebar(Option1):
    st.title('Welcome to HotelCoderFornia')
    st.caption('Made by the RoomReservers!')
    st.subheader(':violet[You are currently are in:]')
    st.subheader(Option1)
    st.warning('🚨Always make sure all fields are field or the system will error🚨 Refresh the page should you run into an error')

#Text for Option3 No
def Option3No():
    st.subheader(' Acknowledged :ok_hand: :ok_hand: :ok_hand:')

#Divder
def divide():
    st.divider()
    st.subheader('Would you like to ammend the following record?')

#Display Option1
def DisplayO1(Option1):
    st.header(Option1)
    if Option1 == 'View Records':st.subheader('Record Viewing')
    else: st.subheader('New Record')

#New Booking Form
def BookingForm(cursor,conn):
    Var2=st.date_input('Enter Arrival Date',dt.datetime.today(),dt.datetime.today(),key=3)
    Var3=st.date_input('Enter Departure Date',dt.datetime.today(),dt.datetime.today(),key=4)
    Var4=st.number_input('Enter Pax',1,value=1,key=5)

    cursor.execute('SELECT ID FROM customers')
    rows= cursor.fetchall()
    customer_id_list= []
    for row in rows:
        column_value = row[0]
        customer_id_list.append(column_value)
    customer_id_list.sort()
    Var5=st.selectbox('Select Customer ID',customer_id_list,key=1)

    cursor.execute('SELECT Hotel_ID FROM room')
    rows= cursor.fetchall()
    room_id_list= []
    for row in rows:
        column_value= row[0]
        room_id_list.append(column_value)
    room_id_list.sort()
    Var6=st.selectbox('Select Room ID',room_id_list,key=2)
    submit=st.form_submit_button('Submit')
    if submit == True:
        Pye.NewBooking(cursor,conn,str(Var2),str(Var3),Var4,Var5,Var6)

#New Customer Form
def CustomerForm(cursor,conn):
    Var2 = st.text_input('Enter First Name',key=6)
    Var3 = st.text_input('Enter Last Name',key=7)
    Var4 =st.text_input('Enter Passport number',max_chars=15,key=8)
    Var5 =st.date_input('Enter Passport Expiration',min_value=dt.datetime.today(),key=9)
    Var6 =st.date_input('Enter Date of birth',dt.datetime.today(),dt.date(1850,1,1),dt.datetime.today(),10)
    Var7 =st.text_input('Enter Phone number',max_chars=15,key=11)
    Var8 =st.text_input('Enter Nationality',key=12)
    Var9 =st.radio('Enter Gender',options=['Male','Female'],horizontal=True,key=13)
    Var10 =st.text_input('Enter e-mail address','',key=14)
    Var11 =st.text_input('Enter credit card',type='password',key=15)
    submit=st.form_submit_button('Submit')
    if submit == True:
        Pye.NewCustomer(cursor,conn,Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11)

#New Guest Form
def GuestForm(cursor,conn):
    Var2=st.text_input('Enter Guest First Name',key=19)
    Var3=st.text_input('Enter Guest Last Name',key=20)
    Var4=st.text_input('Enter Guest Passport',max_chars=15,key=21)
    Var5=st.text_input('Enter any additional notes', key=22)

    cursor.execute('SELECT Booking_ID FROM booking')
    rows= cursor.fetchall()
    booking_id_list= []
    for row in rows:
        column_value= row[0]
        booking_id_list.append(column_value)
    booking_id_list.sort()
    Var6=st.selectbox('Select Booking ID',booking_id_list,key=18)
    
    if len(booking_id_list) == 0:
        submit=st.form_submit_button('Submit',disabled=True)
    else:submit=st.form_submit_button('Submit')
    if submit == True:
        Pye.NewGuest(cursor,conn,Var2,Var3,Var4,Var5,Var6)

#View a booking record
def ViewBookingRecord(cursor):
    st.subheader('View a record')
    cursor.execute('SELECT Booking_ID FROM booking')
    rows= cursor.fetchall()
    booking_id_list=[]
    for row in rows:
        column_value =row[0]
        booking_id_list.append(column_value)
    booking_id_list.sort()
    Option3=st.selectbox('Select **Booking ID** number',booking_id_list,key=23) 
    cursor.execute('SELECT * FROM booking WHERE Booking_ID=%s',(int(Option3)))
    results=cursor.fetchone()
    f.ViewBooking(results)
    f.conversion(results,3,4)

#View a customer record
def ViewCustomerRecord(Option2,cursor):
    st.subheader(Option2)
    Option3=st.selectbox('How would you like to sort by?',('ID','First and Last Name','Passport no.'))
    
    if Option3 == 'ID':
        cursor.execute('SELECT ID FROM customers')
        rows = cursor.fetchall()

        customer_id_list = []

        for row in rows:
            column_value = row[0]
            customer_id_list.append(column_value)

        customer_id_list.sort()

        CustomerID = st.selectbox('Select Customer ID',customer_id_list)
        cursor.execute('SELECT * FROM customers WHERE ID=%s',(CustomerID))
        results=cursor.fetchone()
        f.ViewCustomers(results)
        f.conversion(results,4,5)
    
    elif Option3 == 'First and Last Name':

        with st.form('form'):
            LastName= str(st.text_input('Enter the last Name',key=34))
            FirstName= str(st.text_input('Enter the first Name',key=33))
            submit= st.form_submit_button('Submit')
            if submit == True:
                cursor.execute('SELECT L_Name,F_Name FROM customers')
                rows= cursor.fetchall()
                customer_name_list= []
                for row in rows:
                    column_value= row[0]
                    column_value2 =row[1]
                    customer_name_list.append(column_value + '' + column_value2)
                customer_name_list.sort()
                customer_name_checker = LastName + '' + FirstName

                if customer_name_checker in customer_name_list:
                    cursor.execute('SELECT * FROM customers WHERE F_Name =%s AND L_Name =%s',(FirstName, LastName))
                    results=cursor.fetchone()
                    f.ViewCustomers(results)
                else:st.warning('Entered Customer Name not in Database')
        
    
    elif Option3 == 'Passport no.':
        with st.form('form'):
            Passport=Passport= str(st.text_input('Enter the Passport/IC number',max_chars=15,key=35))
            submit= st.form_submit_button('Submit')
            if submit == True:
                cursor.execute('SELECT Passport_No FROM customers')
                rows= cursor.fetchall()
                passport_no_list= []
                for row in rows:
                    column_value= row[0]
                    passport_no_list.append(column_value)
                passport_no_list.sort()
                if Passport in passport_no_list:
                    cursor.execute('SELECT * FROM customers WHERE Passport_no=%s',(Passport))
                    results=cursor.fetchone()
                    f.ViewCustomers(results)
                else:st.warning('Entered Passport Number not in database')

#View a guest record
def ViewGuestRecord(Option2,cursor):
    st.subheader(Option2)
    Option3= st.selectbox(
        'How would you like to sort by?',
        ('Guest ID', 'First Name and Last Name', 'Passport'))
    
    if Option3 == 'Guest ID':
        cursor.execute('SELECT Guest_ID FROM guest')
        rows= cursor.fetchall()
        Guest_id_list=[]
        for row in rows:
            column_value= row[0]
            Guest_id_list.append(column_value)
        Guest_id_list.sort()
        Option4= st.selectbox('Select the **Guest ID** number',Guest_id_list,key=60)
        cursor.execute('SELECT * FROM guest WHERE Guest_ID=%s',(int(Option4)))
        results=cursor.fetchone()
        f.ViewGuest(results)
        results=str(results)
        st.download_button('Download Results',results)
        
        
    if Option3 == 'First Name and Last Name':
        with st.form('form3'):
            FirstName= str(st.text_input('Enter the First Name','',255,76))
            LastName= str(st.text_input('Enter the Last Name','',255,77))
            submit=st.form_submit_button('Submit')
            if submit == True:
                cursor.execute('SELECT Guest_F_Name,Guest_L_Name FROM guest')
                rows= cursor.fetchall()
                Guest_name_list= []
                for row in rows:
                    column_value= row[0]
                    column_value2 = row[1]
                    Guest_name_list.append(column_value + '' + column_value2)
                Guest_name_list.sort()
                Guest_name_checker =FirstName + '' + LastName
                if Guest_name_checker in Guest_name_list:
                    cursor.execute('SELECT * FROM guest WHERE Guest_F_Name =%s AND Guest_L_Name =%s',(FirstName, LastName))
                    results=cursor.fetchone()
                    f.ViewGuest(results)
                else:st.warning('Entered Guest Name not in Datavase')

    if Option3 == 'Passport':
        with st.form('form4'):
            Passport= str(st.text_input('Enter the Passport/IC number','',255,78))
            submit=st.form_submit_button('Submit')
            if submit == True:
                cursor.execute('SELECT Guest_Passport FROM guest')
                rows= cursor.fetchall()
                passport_no_list= []
                for row in rows:
                    column_value= row[0]
                    passport_no_list.append(column_value)
                passport_no_list.sort()
                if Passport in passport_no_list:
                    cursor.execute('SELECT * FROM guest WHERE Guest_Passport=%s',(Passport))
                    results=cursor.fetchone()
                    f.ViewGuest(results)
                else:st.warning('Entered Passport not in Database')

#View a room record
def ViewRoomRecord(Option2,cursor):
    st.subheader(Option2)
    cursor.execute('SELECT Hotel_ID FROM room')
    rows= cursor.fetchall()
    Room_id_list=[]
    for row in rows:
        column_value= row[0]
        Room_id_list.append(column_value)
    Room_id_list.sort()
    Option4= st.selectbox('Select the **Room ID** number',Room_id_list)
    cursor.execute('SELECT * FROM room WHERE Hotel_ID=%s',(int(Option4)))
    results=cursor.fetchone()
    f.ViewRoom(results)
    results=str(results)
    st.download_button('Download Results',results)


#Update Booking
def UpdateBookingRecord(Option3,cursor,conn):
    if Option3 == 'Yes':
        st.subheader('Record Ammendment')
        cursor.execute('SELECT Booking_ID FROM booking')
        rows= cursor.fetchall()
        Booking_ID_list= []
        for row in rows:
            column_value=row[0]
            Booking_ID_list.append(column_value)
        Booking_ID_list.sort()
        var=st.selectbox('What was the original Booking ID?',Booking_ID_list)
        with st.form('36',True):
            Var2=st.date_input('Enter Arrival Date',dt.datetime.today(),dt.datetime.today(),key=28)
            Var3=st.date_input('Enter Departure Date',dt.datetime.today(),dt.datetime.today(),key=29)
            Var4=st.number_input('Enter Pax',1,value=1,key=30)

            cursor.execute('SELECT ID FROM customers')
            rows= cursor.fetchall()
            customer_id_list= []
            for row in rows:
                column_value = row[0]
                customer_id_list.append(column_value)
            customer_id_list.sort()
            Var5=st.selectbox('Select the **CustomerID**',customer_id_list)

            cursor.execute('SELECT Hotel_ID FROM room')
            rows= cursor.fetchall()
            Room_id_list=[]
            for row in rows:
                column_value= row[0]
                Room_id_list.append(column_value)
            Room_id_list.sort()
            Var6= st.selectbox('Select the **Room ID** number',Room_id_list)
            submit=st.form_submit_button('Submit')
        if submit == True:
            Pye.UpdateBooking(cursor,conn,Var2,Var3,Var4,Var5,Var6,var)
            st.info('Refresh the page to see changes')
    
    if Option3 == 'No':
        Option3No()

#Update Customer
def UpdateCustomerRecord(Option3,cursor,conn):
    if Option3 == 'Yes':
        st.subheader('Record Ammendment')
        cursor.execute('SELECT ID FROM customers')
        rows = cursor.fetchall()
        customer_id_list = []
        for row in rows:
            column_value = row[0]
            customer_id_list.append(column_value)
        customer_id_list.sort()
        var= st.selectbox('Select Customer ID',customer_id_list,key=75)
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
            Pye.UpdateCustomer(cursor,conn,Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11,var)
            st.info('Refresh the page to see changes')
    
    if Option3 == 'No':
        Option3No()

#Update Guest
def UpdateGuestRecord(Option3,cursor,conn):
    if Option3 == 'Yes':
        st.subheader('Record Ammendment')
        cursor.execute('SELECT Guest_ID FROM guest')
        rows= cursor.fetchall()
        Guest_id_list=[]
        for row in rows:
            column_value= row[0]
            Guest_id_list.append(column_value)
        Guest_id_list.sort()
        var=st.selectbox('What was the original Guest ID?',Guest_id_list)
        with st.form('63',True):
            Var2=st.text_input('Enter Guest First Name',key=19)
            Var3=st.text_input('Enter Guest Last Name',key=20)
            Var4=st.text_input('Enter Guest Passport',max_chars=15,key=21)
            Var5=st.text_input('Enter any additional notes', key=22)
            cursor.execute('SELECT Booking_ID FROM booking')
            rows= cursor.fetchall()
            Booking_ID_list= []
            for row in rows:
                column_value=row[0]
                Booking_ID_list.append(column_value)
            Booking_ID_list.sort()
            Var6=st.selectbox('Enter Booking ID',Booking_ID_list)
            submit=st.form_submit_button('Submit')
        if submit == True:
            Pye.UpdateGuest(cursor,conn,Var2,Var3,Var4,Var5,Var6,var)
            st.info('Refresh the page to see changes')

    if Option3 == 'No':
            Option3No()
