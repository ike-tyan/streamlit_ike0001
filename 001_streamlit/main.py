import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image

st.title("Hello, kei!")
st.write("This is a simple Streamlit app.")

df = pd.DataFrame({
'カラム1':[1,2,3,4],
'カラム2':[5,6,7,8]
})

#表＜マジックコマンド＞
df

#表＜writeメソッド＞
st.write(df)

#表＜tableメソッド＞
st.table(df)

#グラフ
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['東京', '大阪', '静岡'])
st.line_chart(chart_data)

#地図
map_data = pd.DataFrame(
    np.random.randn(1000,2)/[50,50]
    +[35.6894, 139.6917],
    columns=['lat', 'lon'])
st.map(map_data)

#ウィジェット・スライダー
x = st.slider('x')
st.write(x,'を２倍にすると',2*x)

#チェックボックス
if st.checkbox('表を見たい時はチェックしてください。'):
    df

#セレクトボックス
option = st.selectbox(
    'お好きな数字を選択してください。',
    [1, 2, 3, 4, 5]
)
'選択した数字は', option, 'ですね(^^♪'

#配置・sidebar
add_selectbox = st.sidebar.selectbox(
    'お好きな文字を選択して！',
    ['あ', 'い', 'う', 'え', 'お']
)

#配置・slider
add_slider = st.sidebar.slider(
    'スライダー',
    0.0, 100.0, (25.0, 75.0)    
)

#コラム・ボタン
left_column, right_column = st.columns(2)
left_column.button('ボタン左')
right_column.button('ボタン右')

# URLから画像表示
image_url = "https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB:Erika_Ikuta_2022_House_of_Councillors_Election_Enlightment_Poster.jpg"

#イメージ画像
Image = Image.open('001_streamlit/k02.jpg')
st.image(Image, caption='笑顔(^^♪')

#音楽
audio_file = open('001_streamlit/voice_193948.m4a', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/m4a')

#動画
video_file = open('001_streamlit/googleVeo2.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

