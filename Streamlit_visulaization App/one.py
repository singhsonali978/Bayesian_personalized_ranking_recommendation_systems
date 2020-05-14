
import sys
import pandas as pd
from PIL import Image
import streamlit as st
import time

st.title('Welcome to world of snack !!!')

    
image = Image.open('snack.jfif')

st.image(image, caption='Snack Recommendation',use_column_width=True)

title = st.number_input('User ID',min_value = 0,max_value=1000,value = 0,step =1)


Type = st.selectbox(
        "Choose Snack Type",["Diet", "Keto","Meats","Vegetarian","Vegan"])


if st.button('Login'):
     data = pd.read_csv(Type+".csv")  
     df1 =  data['UserId']==title
     df2 =data[df1]
     if df2.empty:
         st.write('we have no information on this user!')
         image = Image.open('no.jfif')
         st.image(image,use_column_width=True)
     else:
         image = Image.open('foru.png')
         st.image(image,use_column_width=True)
         st.write(data[df1])
    
    
