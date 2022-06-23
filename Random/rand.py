import streamlit as st
import pandas as pd 
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime
from datetime import datetime as dt
from io import BytesIO
import requests
import urllib.request

#response = requests.get(url)
#img = Image.open(BytesIO(response.content))

#resp = requests.get('https://raw.githubusercontent.com/wlyi1/random/main/Random/rand.png')
#image1 = Image.open('a2.png')
#image2 = Image.open(BytesIO(resp.content))

image1 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/a2.png'
image2 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/a3a.png'
image3 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/dw.png'
image4 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/1.png'
image5 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/2.png'

st.image(image1)
st.image(image2)


list_rand = ['menghitung jumlah ubin', 'push-up 10 x', 'bayarin temen makan', 'mencuci sandal', 'gambar karakter anime']
today_rand = random.choice(list_rand)

st.markdown("----", unsafe_allow_html=True)
columns = st.columns((2, 1, 2))
button_pressed = columns[1].button('Random Me!')
if button_pressed:
    st.write(today_rand)
st.markdown("----", unsafe_allow_html=True)

#download page

hari = dt.today().strftime('%Y-%m-%d')

#font = ImageFont.truetype('Quicksand-Regular.ttf', 55)
#font1 = ImageFont.truetype('Quicksand-Bold.ttf', 28)

img= ImageDraw.Draw(image3)
img.text((80,470), today_rand, fill=(0,0,0))
img.text((450,390), hari, fill=(0,0,0))

if st.button('Show'):
    st.image(image3)

st.markdown("----", unsafe_allow_html=True)
    
st.image(image4)
st.image(image5)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
