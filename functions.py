import datetime as dt
from datetime import datetime
import streamlit as st
import pymysql
import pandas as pd
from io import StringIO

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
    st.download_button('Download results',txt_results)


#File Upload
def filupload():
    upload=st.file_uploader('Upload record','txt',False)
    if upload is not None:
        stringio = StringIO(upload.getvalue().decode("utf-8"))
        string_data = stringio.read()
        without_brackets = ''.join(char for char in string_data if char not in '[](){}<>')
        without_brackets=without_brackets.split(',')

        data = []

        data.append(without_brackets)

        df = []

        if len(without_brackets) == 6 or len(without_brackets) == 11:
            if without_brackets[2].isdigit() == False:
                df=pd.DataFrame(data, columns=['Guest ID', 'Booking ID', 'First Name', 'Last Name', 'Passport Number', 'Notes'])
            else:

                arrival_date_obj = datetime(int(without_brackets[3]), int(without_brackets[4]), int(without_brackets[5]))
                departure_date_obj = datetime(int(without_brackets[6]), int(without_brackets[7]), int(without_brackets[8]))

                data = []

                data.append(without_brackets[0])
                data.append(without_brackets[1])
                data.append(without_brackets[2])
                data.append(arrival_date_obj)
                data.append(departure_date_obj)
                data.append(without_brackets[9])
                # data.append(without_brackets[10])

                data_pass = []

                data_pass.append(data)

                df=pd.DataFrame(data_pass, columns=['Booking ID', 'Customer ID', 'Room ID', 'Arrival Date', 'Departure Date', 'Person'])
        elif len(without_brackets) == 15:
            passport_expiry_date_obj = datetime(int(without_brackets[3]), int(without_brackets[4]), int(without_brackets[5]))
            date_of_birth_date_obj = datetime(int(without_brackets[6]), int(without_brackets[7]), int(without_brackets[8]))

            data = []

            data.append(without_brackets[0])
            data.append(without_brackets[1])
            data.append(without_brackets[2])
            data.append(without_brackets[3])
            data.append(passport_expiry_date_obj)
            data.append(date_of_birth_date_obj)
            data.append(without_brackets[9])
            data.append(without_brackets[10])
            data.append(without_brackets[11])
            data.append(without_brackets[12])
            data.append(without_brackets[13])

            data_pass = []

            data_pass.append(data)

            df=pd.DataFrame(data_pass, columns=['Customer ID', 'Last Name', 'First Name', 'Passport Number', 'Passport Expiry', 'Date of Birth','Phone Number','Nationality','Gender','Email','Credit Card Number'])
        
        elif len(without_brackets) == 8:
            data = []

            data.append(without_brackets[0])
            data.append(without_brackets[1])
            data.append(without_brackets[2])
            data.append(without_brackets[3])
            data.append(without_brackets[4])
            data.append(without_brackets[5])
            data.append(without_brackets[6])

            data.append(without_brackets[7])

            data_pass = []

            data_pass.append(data)

            df=pd.DataFrame(data_pass, columns=['Room ID', 'Number of Beds', 'Bed Type', 'Price', 'Minibar', 'Entertainment System','Bath Tub','Notes'])
        

        st.table(df)


#View Booking result
def ViewBooking(results):
    data= []
    data.append(results)
    df= pd.DataFrame(data, columns=['BookingID', 'Customer ID', 'Hotel ID', 'Arrival Date', 'Departure Date', 'Number of Person'])
    st.table(df)

#View Customer Result
def ViewCustomers(results):
    data=[]
    data.append(results)
    df=pd.DataFrame(data, columns=['Customer ID', 'Last Name', 'First Name', 'Passport Number', 'Passport Expiry', 'Date of Birth', 'Phone Number', 'Nationality','Sex', 'Email', 'Credit Card'])
    st.table(df)    

#View Guest Result
def ViewGuest(results):
    data=[]
    data.append(results)
    df=pd.DataFrame(data, columns=['Guest ID','Booking ID','Guest First Name','Guest Last Name','Guest Passport','Guest Notes'])
    st.table(df)

#View Room Result
def ViewRoom(results):
    data=[]
    data.append(results)
    df=pd.DataFrame(data,columns=['Hotel_ID','Beds','Bed Type','Price','Minibar','Entertainment Sytem','Bathtub','Addional Notes'])
    st.table(df)