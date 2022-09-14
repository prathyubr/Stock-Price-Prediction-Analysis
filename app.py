import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(layout="wide")
df=pd.read_csv('Stock Data_CSV.csv')
#Explore data
st.title ('Stock Trend Prediction') 
st.write(df)
df.head()
df.tail()
df1=pd.read_csv('RELIANCE_Data.csv')
st.write(df1.head())
st.write(df1.tail())
df2=pd.read_csv('SBIN_Data.csv')
st.write(df2.head())
st.write(df2.tail())
df3=pd.read_csv('TATA_Data.csv')
st.write(df3.head())
st.write(df3.tail())
df4=pd.read_csv('TCS_Data.csv')
st.write(df4.head())
st.write(df4.tail())
df5=pd.read_csv('WIPRO_Data.csv')
st.write(df5.head())
st.write(df5.tail())
st.line_chart(df['HIGH'])
st.line_chart(df['52W H'])
st.line_chart(df['52W L'])
st.line_chart(df['VOLUME'])
st.line_chart(df1['CLOSE'])
st.line_chart(df2['CLOSE'])
st.line_chart(df3['CLOSE'])
st.line_chart(df4['CLOSE'])
st.line_chart(df5['CLOSE'])
from PIL import Image
image = Image.open('image1.jpeg')
st.image(image,caption='Actual Prices VS Predicted Prices using Linear regression')
from PIL import Image
image = Image.open('image2.jpeg')
st.image(image,caption='Shift train & test predictions for plotting')
from PIL import Image
image = Image.open('image3.jpeg')
st.image(image,caption='Stock Prediction for next 10 days')
from PIL import Image
image = Image.open('image4.jpeg')
st.image(image,caption='Stocks moving average from CLOSE and OPEN prices')
#Add a visualization bar on the left
# Object notation
with st.sidebar:
 st.header('GROUP-2')
 st.subheader('Participants')
 st.write('Abhinand Saravanan')
 st.write('RohanChandrakantAwate')
 st.write('MohanrajB')
 st.write('Prathyush B R')
 st.write('Mohammed Usama M B')
 st.write('Sandeep Raju C')
 st.header('Mentor/Guided By')
 st.write('Karthik Sir')
 st.write('Dhanyapriya Mam')
 
 
