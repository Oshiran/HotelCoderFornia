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

#New Customer Form
def CustomerForm(cursor,conn):
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
        Pye.NewCustomer(cursor,conn,Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11)

#New Booking Form
def BookingForm(cursor,conn):
    Var2=st.number_input('Enter Customer ID',1,step=1,key=1)
    Var3=st.number_input('Enter Room ID',1,step=1,key=2)
    Var4=st.date_input('Enter Arrival Date',dt.datetime.today(),dt.datetime.today(),key=3)
    Var5=st.date_input('Enter Departure Date',dt.datetime.today(),dt.datetime.today(),key=4)
    Var6=st.number_input('Enter Pax',1,value=1,key=5)
    submit=st.form_submit_button('Submit')
    if submit == True:
        Pye.NewBooking(cursor,conn,Var2,Var3,Var4,Var5,Var6)

#New Guest Form
def GuestForm(cursor,conn):
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
        Pye.NewGuest(cursor,conn,Var2,Var3,Var4,Var5,Var6,Var7,Var8)

#View a booking record
def ViewBookingRecord(cursor):
    st.subheader('View a record')
    Option3=st.number_input('Enter the **Booking ID** number',1,None,1,1,key=23) 
    cursor.execute('SELECT * FROM booking WHERE Booking_ID=%s',(int(Option3)))
    results=cursor.fetchone()
    f.ViewBooking(results)
    f.conversion(results,3,4)

#View a customer record
def ViewCustomerRecord(Option2,cursor):
    st.subheader(Option2)
    Option3=st.selectbox('How would you like to sort by?',('ID','First and Last Name','Passport no.'))
    
    if Option3 == 'ID':
        CustomerID=int(st.number_input('Enter the **Customer ID** number',1,None,1,1,key=32))
        cursor.execute('SELECT * FROM customers WHERE ID=%s',(CustomerID))
        results=cursor.fetchone()
        f.ViewCustomers(results)
        f.conversion(results,4,5)
    
    elif Option3 == 'First and Last Name':
        FirstName= str(st.text_input('Enter the first Name',key=33))
        LastName= str(st.text_input('Enter the last Name',key=34))
        cursor.execute('SELECT * FROM customers WHERE F_Name =%s AND L_Name =%s',(FirstName, LastName))
        results=cursor.fetchone()
        f.ViewCustomers(results)
        
    
    elif Option3 == 'Passport no.':
        Passport=Passport= str(st.text_input('Enter the Passport/IC number',max_chars=15,key=35))
        cursor.execute('SELECT * FROM customers WHERE Passport_no=%s',(Passport))
        results=cursor.fetchone()
        f.ViewCustomers(results)

#View a guest record
def ViewGuestRecord(Option2,cursor):
    st.subheader(Option2)
    Option3= st.selectbox(
        'How would you like to sort by?',
        ('Guest ID', 'First Name and Last Name', 'Passport'))
    
    if Option3 == 'Guest ID':
        Option4= st.number_input('Enter the **Guest ID** number',1,None,1,1,key=60)
        cursor.execute('SELECT * FROM guest WHERE Guest_ID=%s',(int(Option4)))
        f.ViewGuest(cursor)
        
    if Option3 == 'First Name and Last Name':
        FirstName= str(st.text_input('Enter the first Name','',255,43))
        LastName= str(st.text_input('Enter the last Name','',255,44))
        cursor.execute('SELECT * FROM guest WHERE Guest_F_Name =%s AND Guest_L_Name =%s',(FirstName, LastName))
        f.ViewGuest(cursor)

    if Option3 == 'Passport':
        Passport= str(st.text_input('Enter the Passport/IC number','',255,45))
        cursor.execute('SELECT * FROM guest WHERE Guest_Passport=%s',(Passport))
        f.ViewGuest(cursor)

#View a room record
def ViewRoomRecord(Option2,cursor):
    st.subheader(Option2)
    Option3 = st.number_input('Enter the **Room ID** number',1,None,1)
    f.ViewRoom(cursor,Option3)

#Update Booking
def UpdateBookingRecord(Option3,cursor,conn):
    if Option3 == 'Yes':
        st.subheader('Record Ammendment')
        var=st.number_input('What was the original Booking ID?',1,value=1,step=25)
        with st.form('36',True):
            Var2=st.number_input('Enter Customer ID',1,step=1,key=26)
            Var3=st.number_input('Enter Room ID',1,step=1,key=27)
            Var4=st.date_input('Enter Arrival Date',dt.datetime.today(),dt.datetime.today(),key=28)
            Var5=st.date_input('Enter Departure Date',dt.datetime.today(),dt.datetime.today(),key=29)
            Var6=st.number_input('Enter Pax',1,value=1,key=30)
            submit=st.form_submit_button('Submit')
        if submit == True:
            Pye.UpdateBooking(cursor,conn,Var2,Var3,Var4,Var5,Var6,var)
    
    if Option3 == 'No':
        Option3No()

#Update Customer
def UpdateCustomerRecord(Option3,cursor,conn):
    if Option3 == 'Yes':
        st.subheader('Record Ammendment')
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
            Pye.UpdateCustomer(cursor,conn,Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11,var)
    
    if Option3 == 'No':
        Option3No()

#Update Guest
def UpdateGuestRecord(Option3,cursor,conn):
    if Option3 == 'Yes':
        st.subheader('Record Ammendment')
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
            Pye.UpdateGuest(cursor,conn,Var2,Var3,Var4,Var5,Var6,Var7,Var8,var)

        if Option3 == 'No':
            Option3No()
