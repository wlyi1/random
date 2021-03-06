import streamlit as st
import pandas as pd
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime
from datetime import datetime as dt

image1 = Image.open('a2.png')
image2 = Image.open('a3a.png')

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

image = Image.open('dw.png')
font = ImageFont.truetype('Quicksand-Regular.ttf', 55)
font1 = ImageFont.truetype('Quicksand-Bold.ttf', 28)

list_rand = ['menghitung jumlah ubin', 'push-up 10 x', 'bayarin temen makan', 'mencuci sandal', 'gambar karakter anime']
text = random.choice(list_rand)

img= ImageDraw.Draw(image)
img.text((80,470), text, font = font, fill=(0,0,0))
img.text((450,390), hari, font = font1, fill=(0,0,0))

total_img = [x for x in range(1000)]
n = 0
if n < 1000:
    image = image.save(f'myimage{n}.png')
    n += 1

with open(f"myimage{n-1}.png", "rb") as file:
     btn = st.download_button(
             label="Download image",
             data=file,
             file_name=f"{hari}.png",
             mime="image/png"
           )



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)