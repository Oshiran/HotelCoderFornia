import pymysql
import streamlit as st

#New Booking 
def NewBooking(cursor,conn,Var2,Var3,Var4,Var5,Var6):
    cursor.execute('INSERT INTO booking(ID, Hotel_ID, Arrival_Date, Departure_Date, Pax) VALUES (%s, %s, %s, %s, %s)',(Var2,Var3,Var4,Var5,Var6))
    conn.commit()
    st.write('Record entered')
    st.info('Listed below are information you have entered')
    st.write(Var2,Var3,Var4,Var5,Var6)
    st.write('Record entered')
    st.balloons()

#New Customer
def NewCustomer(cursor,conn,Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11):
    cursor.execute('INSERT INTO customers(L_name, F_Name, Passport_No, Passport_Exp, DOB, Phone_no, Nationality, Sex, Email, Credit_Card) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11))
    conn.commit()
    st.write('Record entered')
    st.info('Listed below are information you have entered')
    st.write(Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11)
    st.balloons()

#New Guest
def NewGuest(cursor,conn,Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9):
    cursor.execute('INSERT INTO guest(Guest_ID, ID, Hotel_ID, Booking_ID, Guest_F_Name, Guest_L_Name, Guest_Passport, G_notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',(Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9))
    conn.commit()
    st.write('Record entered')
    st.info('Listed below are information you have entered')
    st.write(Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9)
    st.balloons()
    st.write('Record entered')
    st.balloons()

#Update Booking
def UpdateBooking(cursor,conn,Var2,Var3,Var4,Var5,Var6,var):
    cursor.execute('UPDATE booking SET ID=%s, Hotel_ID=%s, Arrival_Date=%s, Departure_Date=%s, Pax=%s WHERE Booking_ID=%s',(Var2,Var3,Var4,Var5,Var6,var))
    conn.commit()
    st.write('Record Updated')
    st.info('Listed below are information you have entered')
    st.write(Var2,Var3,Var4,Var5,Var6,var)
    st.balloons()

#Update Customer
def UpdateCustomer(cursor,conn,Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11,var):
    cursor.execute('UPDATE customers SET F_Name=%s, L_Name=%s, Passport_No=%s, Passport_Exp=%s, DOB=%s, Phone_no=%s, Nationality=%s, Sex=%s, Email=%s, Credit_Card=%s WHERE ID=%s',(Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11,var))
    conn.commit()
    st.write('Record Updated')
    st.info('Listed below are information you have entered')
    st.write(var,Var2,Var3,Var4,Var5,Var6,Var7,Var8,Var9,Var10,Var11)
    st.balloons()

#Update Guest
def UpdateGuest(cursor,conn,Var2,Var3,Var4,Var5,Var6,Var7,Var8,var):
    cursor.execute('UPDATE guest SET ID=%s, Hotel_ID=%s, Booking_ID=%s, Guest_F_Name=%s, Guest_L_Name=%s, Guest_Passport=%s, G_notes=%s WHERE Guest_ID=%s',(Var2,Var3,Var4,Var5,Var6,Var7,Var8,var))
    conn.commit()
    st.write('Record Updated')
    st.info('Listed below are information you have entered')
    st.write(Var2,Var3,Var4,Var5,Var6,Var7,Var8,var)
    st.balloons()

#Describe Booking
def DescribeBooking(Option2,cursor):
    st.subheader(Option2)
    cursor.execute('Describe Booking')
    results=cursor.fetchall()
    st.table(results)

#Describe Customer
def DescribeCustomers(Option2,cursor):
    st.subheader(Option2)
    cursor.execute('Describe Customers')
    results=cursor.fetchall()
    st.table(results)

#Describe Guest
def DescribeGuest(Option2,cursor):
    st.subheader(Option2)
    cursor.execute('Describe Guest')
    results=cursor.fetchall()
    st.table(results)

#Describe Room
def DescribeRoom(Option2,cursor):
    st.subheader(Option2)
    cursor.execute('Describe Room')
    results=cursor.fetchall()
    st.table(results)


