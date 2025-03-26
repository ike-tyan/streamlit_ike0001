# streamlit run  "C:\Users\ikega\OneDrive\デスクトップ\001_streamlit_0test\pages\page_01.py"

import streamlit as st
import os
from PIL import Image

st.title('ページ1')

#poto1 = Image.open(r"C:\Users\ikega\OneDrive\デスクトップ\001_streamlit_0test\data\k02.jpg")
#st.image(poto1,width=100)

# 相対パスの生成
# 現在のファイルのディレクトリを取得
current_dir1 = os.path.dirname(__file__)

# 上記のディレクトリの親ディレクトリを取得
current_dir2 = os.path.dirname(current_dir1)

# 親ディレクトリを取得から作りたいパスを作成
poto2 = os.path.join(current_dir2, 'data', 'k02.jpg')

# Streamlitで画像を表示
st.image(poto2, width=50, caption="カレントディレクトリから絶体パスを作成")


