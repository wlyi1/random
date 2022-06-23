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


req_img_1 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/rand.png'
#image1 = Image.open('a2.png')
#image2 = Image.open('a3a.png')

st.image(req_img_1)
#st.image(image2)

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

#image = Image.open('dw.png')
#font = ImageFont.truetype('Quicksand-Regular.ttf', 55)
#font1 = ImageFont.truetype('Quicksand-Bold.ttf', 28)

#list_rand = ['menghitung jumlah ubin', 'push-up 10 x', 'bayarin temen makan', 'mencuci sandal', 'gambar karakter anime']
#text = random.choice(list_rand)

img= ImageDraw.Draw(req_img_1)
img.text((80,470), today_rand, fill=(0,0,0))
img.text((450,390), hari, fill=(0,0,0))

#total_img = [x for x in range(1000)]
#n = 0
#if n < 1000:
    #image = image.save(f'myimage{n}.png')
    #n += 1

with open(req_img_1, "rb") as file:
     btn = st.download_button(
             label="Download image",
             data=file,
             file_name="flower.png",
             mime="image/png"
           )


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
