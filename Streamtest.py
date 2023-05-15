import streamlit as st
import pandas as pd

# df= pd.DataFrame({ 'first column': [1,2,3,4], 'second column':[10,20,30,40]})


# option = st.selectbox('which number do you like best?',
# df['first column'])

# 'you selected:', option

# option = st.selectbox(
#     'Which table would you like to edit?',
#     ('Customer', 'Hotel Room', 'Booking', 'Guest'))


            
Var9 =st.select_slider(
'Enter Gender',
options=['Male','Female'],
key=18)
st.write(Var9)

# color = st.select_slider(
#     'Select a color of the rainbow',
#     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
#     value=['red','violet'],
#     )
# st.write('My favorite color is', color)


# City_options = {
# 5: "Arizona Chandler - 5",
# 4: "Arizona Phoenix -4",
# 3: "New Jersey Newark -3",
# 2: "Oregon Portland -2",
# 1: "Seattle Washington -1",
# }

# city_mode=st.sidebar.radio(
# label="Choose a city option:",
# options=(5, 4, 3, 2, 1), 
# format_func=lambda x: City_options.get(x),
# )

# st.write(f'You have chosen {City_options.get(city_mode)}'
#          f' with the value {city_mode}.')

Var5 =st.date_input('Enter Passport Expiration',None,None,None,14)
st.write(Var5)