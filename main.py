import pymysql
import streamlit as st
import functions as f
import GUI
import PYSQLexec as Pye

GUI.Setup()
# Establish a connection to the SQL Server database and create a cursor object to interact with the database
conn = pymysql.connect(db='hotel_database', user='root', passwd='', host='localhost', port=3306)
cursor = conn.cursor()

st.title('Welcome to Room Reservers, Hotel CoderFornia')
Option1= st.selectbox('What would you like to do?',('Booking', 'View Records'))

#Do a booking or view a record
if Option1 == 'Booking':
    GUI.DisplayO1(Option1)
    Option2=st.selectbox('Which new would you like to make',('Booking','Customer','Guest',))

    #New Booking record
    if Option2 == "Booking":
        GUI.BookingForm(cursor,conn)
        st.subheader('New Booking Record')
        with st.form('21',True):
            GUI.BookingForm(cursor,conn)

    #New Customer Record
    if Option2 == "Customer":
        st.subheader('New Customer Record')
        with st.form('10',True):
            GUI.CustomerForm(cursor,conn)

    #New Guest Record
    if Option2 == "Guest":
        st.subheader('New Guest Record')
        with st.form('28',True):
            GUI.GuestForm(cursor,conn)

    #View Records
elif Option1 == 'View Records':
    GUI.DisplayO1(Option1)
    #Seperate tabs for each table for ease
    tab1, tab2, tab3, tab4, tab5 = st.tabs([':blue[**Booking**]', ':blue[**Customers**]', ':blue[**Guest**]', ':blue[**Room**]', ':blue[**Upload**]'])

    #View Booking
    with tab1:
        st.subheader('Table: Booking')
        Option2= st.selectbox(
            'What would you like to do?',
            ('View a record','Describe a table')) 
        
        if Option2 == 'Describe a table':
            Pye.DescribeBooking(Option2,cursor)
        elif Option2 == 'View a record':
            GUI.ViewBookingRecord(cursor)
            GUI.divide()
            #Update Booking
            Option3=st.radio('Select',['No','Yes'], horizontal=True,key=24)
            with st.expander('Ammend record',True):
                GUI.UpdateBookingRecord(Option3,cursor,conn)
                 
    #View Customers
    with tab2:
        st.subheader('Table: Customers')
        Option2= st.selectbox('Which option would you like to run?',('View a record','Describe a table'),0,str,key=31) 
        
        if Option2 == 'Describe a table':
            Pye.DescribeCustomers(Option2,cursor)
        elif Option2 == 'View a record':
            GUI.ViewCustomerRecord(Option2,cursor)
            GUI.divide()
            #Update Customer
            Option3=st.radio('Select',['No','Yes'], horizontal=True,key=62)
            with st.expander('Ammend record',True):
                GUI.UpdateCustomerRecord(Option3,cursor,conn)

    #View Guest
    with tab3:
        st.subheader('Table: Guest')
        Option2= st.selectbox('Which option would you like to run?',('View a record','Describe a table'),0,str,3)

        if Option2 == 'Describe a table':
            Pye.DescribeGuest(Option2,cursor)

        elif Option2 == 'View a record':
            GUI.ViewGuestRecord(Option2,cursor)
            GUI.divide()

            #Update Guest
            Option3=st.radio('Select',['No','Yes'], horizontal=True,key=61)
            with st.expander('Ammend record',True):
                GUI.UpdateGuestRecord(Option3,cursor,conn)
    
    #View Room
    with tab4:
        st.subheader('Table: Room')
        Option2= st.selectbox(
            'Which option would you like to run?',
            ('View a record', 'Describe a table'),0,str,4)
        
        if Option2 == 'Describe a table':
            Pye.DescribeRoom(Option2,cursor)
        elif Option2 == 'View a record':
           GUI.ViewRoomRecord(Option2,cursor)

    #file uploader
    with tab5:
        upload=st.file_uploader('Upload record','txt',False)
        f.filupload(upload)

with st.sidebar:
    GUI.sidebar(Option1)

# Close the cursor and connection
cursor.close()
conn.close()
