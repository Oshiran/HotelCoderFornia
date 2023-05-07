import streamlit as st
import pandas as pd

df= pd.DataFrame({ 'first column': [1,2,3,4], 'second column':[10,20,30,40]})


option = st.selectbox('which number do you like best?',
df['first column'])

'you selected:', option

option = st.selectbox(
    'Which table would you like to edit?',
    ('Customer', 'Hotel Room', 'Booking', 'Guest'))

st.write('You selected:', option)
