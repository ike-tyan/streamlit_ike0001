
# streamlit run  "C:\Users\ikega\OneDrive\デスクトップ\001_streamlit\main.py"

import streamlit as st
import pandas as pd

from PIL import Image


#画面を左右に分解
left1_column, right1_column = st.columns(2)

with left1_column:
    #左側
    #イメージ画像
    #photo1 = Image.open(r'c:\Users\ikega\OneDrive\デスクトップ\001_streamlit\レシート_001.jpg')
    #ローカルOK
    #photo = Image.open('レシート_001.jpg')
    #ローカルOK、クラウドno
    #photo = Image.open('./レシート_001.jpg')
    
    # 変数Localの値を選択
    # 1＜ローカル＞または2＜クラウド＞を選べるようにする
    Local = 1
    
    # Localの値によって異なるパスを指定
    if Local == 1:
        photo = Image.open(r'c:\Users\ikega\OneDrive\デスクトップ\001_streamlit\レシート_001.jpg')
    elif Local == 2:
        photo = Image.open('001_streamlit/レシート_001.jpg')
    
    #画像の表示
    st.image(photo, caption='レシート類')

with right1_column:
    #右側
    #タイトル
    #st.title("仕訳確認S")
    
    # 赤い文字でタイトルを表示する
    st.markdown(
        "<h1 style='color: red;'>AI-OCR仕訳<BR>確認システム</h1>",
        unsafe_allow_html=True
    )
    #説明文
    #st.write("AI-OCRの結果を現物を見て確認&訂正")
    st.markdown(
        "<h6 style='color: blue;'>AI-OCRの結果を現物を見て確認&訂正</h6>",
        unsafe_allow_html=True
    )

    #テキストボックス(単純)車両費
    kamoku = st.selectbox('科目',('消耗品費', '車両費', '旅費交通費'))
    yy = st.text_input('令和','7')
    mmdd= st.text_input('月日(mmdd)','1231')

    #テキストボックス(3桁カンマ)
    # テキストボックスの値を管理するためのセッション状態の初期化
    if "formatted_value" not in st.session_state:
        st.session_state.formatted_value = "1,000"

    # テキストボックスの作成
    def update_textbox():
        try:
        # 入力値を取得して整数に変換し、3桁カンマ区切りにフォーマット
            input_value = int(st.session_state.input_box)
            st.session_state.formatted_value = "{:,}".format(input_value)
        except ValueError:
            st.session_state.formatted_value = st.session_state.input_box  # 無効な値の場合そのまま維持

    right1_column.text_input(
        "金額",
        value=st.session_state.formatted_value,
        key="input_box",
        on_change=update_textbox
    )


    #テキストボックス(単純)
    t_banngou = st.text_input('登録番号','T1234567890123')
    tekiyou1 = st.text_input('摘要1','セブンイレブン静岡森下町店')
    tekiyou2 = st.text_input('摘要2','来客用缶コーヒー')



#ボタンを横に並べる
left_column, right_column = st.columns(2)
left_column.button('ボタン左')
right_column.button('ボタン右')

