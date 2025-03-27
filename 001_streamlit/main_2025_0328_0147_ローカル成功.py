# streamlit run  "C:\Users\ikega\OneDrive\デスクトップ\001_streamlit\main.py"

import os
import streamlit as st
import streamlit_authenticator as stauth
import yaml
import pandas as pd
from PIL import Image
from yaml.loader import SafeLoader
from datetime import datetime

## 相対パスの生成
# 現在のファイルのディレクトリを取得
current_dir1 = os.path.dirname(__file__)
# 上記のディレクトリの親ディレクトリを取得
#current_dir2 = os.path.dirname(current_dir1)

## 【ログイン機能】ユーザー設定読み込み
# 現在のディレクトリを取得から作りたいパスを作成
yaml_path = os.path.join(current_dir1, 'config.yaml')
with open(yaml_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie_name=config['cookie']['name'],
    cookie_key=config['cookie']['key'],
    cookie_expiry_days=config['cookie']['expiry_days'],
)

## 【ログ作成機能】CSVファイルへの保存用関数
# 現在のディレクトリを取得から作りたいパスを作成
login_history1 = os.path.join(current_dir1, 'login_history.csv')
#関数定義
def save_to_csv(data, filename= login_history1):
    try:
        # 既存のデータを読み込み
        df = pd.read_csv(filename)
        new_df = pd.DataFrame(data)
        # データを追加して保存
        updated_df = pd.concat([df, new_df], ignore_index=True)
        updated_df.to_csv(filename, index=False)
        
    except FileNotFoundError:
        # CSVファイルがない場合、新規作成
        new_df = pd.DataFrame(data)
        new_df.to_csv(filename, index=False)


## UI 
authenticator.login()
if st.session_state["authentication_status"]:
    ## ログイン成功
    with st.sidebar:
        st.markdown(f'## Welcome *{st.session_state['name']}*')
        authenticator.logout('Logout', 'sidebar')
        st.divider()
        #変数に入れておかないと['name']等は直接使えない！
        login_name = {st.session_state['name']}
        st.markdown(
            "<h12 style='color: blue;'>login_name さん【ログイン済み】</h12>",
            unsafe_allow_html=True
        )
        # 現在の日時を取得
        login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.success(f"{login_name} さんが {login_time} にログインしました！")
        # データを保存
        data1 = [{"username": login_name, "login_time": login_time, "page": "P01"}]
        save_to_csv(data1)
        st.write(f"{login_name} さんがのログイン履歴が {login_time} に保存されました！")
        # 現在のディレクトリを取得から作りたいパスを作成
        poto1 = os.path.join(current_dir1, 'data', 'k01.jpg')
        # Streamlitで画像を表示
        st.image(poto1, width=100, caption="パス：" + poto1)



    #画面を左右に分解
    left1_column, right1_column = st.columns(2)

    with left1_column:
         # 現在のディレクトリを取得から作りたいパスを作成
        photo0 = os.path.join(current_dir1, 'data', 'レシート_001.jpg')
        #画像の表示
        st.image(photo0, caption='レシート類')

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
    

elif st.session_state["authentication_status"] is False:
    ## ログイン成功ログイン失敗
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    ## デフォルト
    st.warning('Please enter your username and password')






