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

def _font_as_bytes():
    with open('https://raw.githubusercontent.com/wlyi1/random/main/Random/Quicksand-Regular.ttf', 'rb') as f:
        font_bytes = BytesIO(f.read())
    return font_bytes
#response = requests.get(url)
#img = Image.open(BytesIO(response.content))

resp = requests.get('https://raw.githubusercontent.com/wlyi1/random/main/Random/dw.png')
#image1 = Image.open('a2.png')
image3 = Image.open(BytesIO(resp.content))

image1 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/a2.png'
image2 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/a3a.png'
#image3 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/dw.png'
image4 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/1.png'
image5 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/2.png'

st.image(image1)
st.image(image2)


list_rand = ['menghitung jumlah ubin', 'push-up 10 x', 'bayarin temen makan', 'mencuci sandal', 'gambar karakter anime']
today_rand = random.choice(list_rand)

st.markdown("----", unsafe_allow_html=True)
columns = st.columns((2, 1, 2))
button_pressed = columns[1].button('Random Me!')


#download page
@st.cache(allow_output_mutation=True)
def get_data_input():
    return[]

tgl_random = datetime.datetime.now()

hari = dt.today().strftime('%Y-%m-%d')
path_font = "Random/Quicksand-Regular.ttf"
path_font_2 = 'Random/Quicksand-Bold.ttf'
font = ImageFont.truetype(path_font, 55)
font1 = ImageFont.truetype(path_font_2, 28)

img= ImageDraw.Draw(image3)
img.text((80,470), today_rand, font=font, fill=(0,0,0))
img.text((450,390), hari, font=font1, fill=(0,0,0))

data ='https://raw.githubusercontent.com/wlyi1/random/main/Random/rand1.csv'

if button_pressed:
    st.image(image3)
    get_data_input().append({'Tanggal Random': tgl_random, 'Random':today_rand})
    rand = pd.DataFrame(get_data_input())
    rand.tail(1).to_csv('randoms.csv', mode='a', index = False, header = False)

st.markdown("----", unsafe_allow_html=True)

df = pd.read_csv('randoms.csv', columns=['Tanggal', 'Random'])
st.write(df)
st.header('3 Aktivitas Random Terakhir')
st.caption('tiga list random oleh 3 pengunjung terakhir di RandomKu')

st.info(df['Random'][len(df)-1])
st.success(df['Random'][len(df)-2])
st.warning(df['Random'][len(df)-3])
    
with st.form("my_form"):
    st.write("Ceritain ke RandomKu dong tentang aktivitas randommu hari ini 😃")
    nama = st.text_input("Nama kakak? ")
    cerita = st.text_input("Cerita singkatnya gimana nih?")

   # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        user_ = get_data_input()
        user_.append({'Tanggal Random': tgl_random, 'Nama':nama, 'Input':cerita})
        user = pd.DataFrame(user_)
        user.tail(1).to_csv('user_out.csv', mode='a', index = False, header = False)
        
us = pd.read_csv('user_out.csv')        
st.write(us)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
