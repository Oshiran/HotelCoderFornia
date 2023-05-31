import datetime as dt
import streamlit as st
import pymysql

#Conversion of results to string
def conversion(results,x,y):
    dob_departure = results[x]
    dob_arrival = results[y]

    dob_arrival_list = [dob_arrival.year, dob_arrival.month, dob_arrival.day]
    dob_departure_list = [dob_departure.year, dob_departure.month, dob_departure.day]

    txt_results = ""
    for number in range(len(results)):
        if number < 3:
            txt_results += str(results[number]) + ","
        elif number == x:
            for item in dob_arrival_list:
                txt_results += str(item) + ","
        elif number == y:
            for item in dob_departure_list:
                txt_results += str(item) + ","
        elif number >= 5:
            txt_results += str(results[number])+ ","
        
    st.write(txt_results)
    st.download_button('Download results',txt_results)

#File Upload
def filupload(upload):
    if upload is not None:
        upload=upload.read()
        st.write(upload)

#View Booking result
def ViewBooking(results):
    st.table(results)
    st.info(':exclamation: Results are displayed in the following order:')
    st.info('Booking ID, Customer ID, Hotel_ID, Arrival Date, Departure Date, Pax')

#View Customer Result
def ViewCustomers(results):
    st.table(results)
    st.info(':exclamation: Results are displayed in the following order:')
    st.info('ID,Last Name, First Name, Passport Number, Passport Expiry, Date of birth, Phone no., Nationaility, Sex, Email, Credit Card')      

#View Guest Result
def ViewGuest(cursor):
    results=cursor.fetchone()
    st.table(results)
    st.info(':exclamation: Results are displayed in the following order:')
    st.info('Guest ID, Customer ID, Hotel ID, Booking ID, Guest First Name, Guest Last Name, Guest Passport, Additional Notes')
    results=str(results)
    st.download_button('Download results',results)

#View Room Result
def ViewRoom(cursor,Option3):
    cursor.execute('SELECT * FROM room WHERE Hotel_ID=%s',(int(Option3)))
    results=cursor.fetchone()
    st.table(results)
    st.info(':exclamation: Results are displayed in the following order:')
    st.info('Hotel ID, Beds, Type of Bed, Price, Minibar included, Entertainment System, Bathtub, Notes')
    results=str(results)
    st.download_button('Download results',results)