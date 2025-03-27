# streamlit run  "C:\Users\ikega\OneDrive\デスクトップ\001_streamlit_0test\pages\page_01.py"

import streamlit as st
import streamlit_authenticator as stauth
import yaml
import pandas as pd

from datetime import datetime
from PIL import Image
from yaml.loader import SafeLoader

## ユーザー設定読み込み
yaml_path = r"C:\Users\ikega\OneDrive\デスクトップ\001_streamlit_0test\confug.yaml"

with open(yaml_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie_name=config['cookie']['name'],
    cookie_key=config['cookie']['key'],
    cookie_expiry_days=config['cookie']['expiry_days'],
)

# CSVファイルへの保存用関数
def save_to_csv(data, filename="login_history.csv"):
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


# アプリケーションのメインロジック
## UI 
authenticator.login()
if st.session_state["authentication_status"]:
    ## ログイン成功
    with st.sidebar:
        st.markdown(f'## Welcome *{st.session_state['name']}*')
        authenticator.logout('Logout', 'sidebar')
        st.divider()
    #st.write('# ログインしました!')
    login_name = {st.session_state['name']}
    st.markdown(
        "<h12 style='color: blue;'>login_name さん【ログイン済み】</h12>",
        unsafe_allow_html=True
    )
    st.title('ページ2')
    
    # 現在の日時を取得
    login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.success(f"{login_name} さんが {login_time} にログインしました！")
    # データを保存
    data = [{"username": login_name, "login_time": login_time}]
    save_to_csv(data)
    st.write(f"{login_name} さんがのログイン履歴が {login_time} に保存されました！")

    poto = Image.open(r"C:\Users\ikega\OneDrive\デスクトップ\001_streamlit_0test\data\k02.jpg")
    st.image(poto,width=50)


elif st.session_state["authentication_status"] is False:
    ## ログイン成功ログイン失敗
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    ## デフォルト
    st.warning('Please enter your username and password')






