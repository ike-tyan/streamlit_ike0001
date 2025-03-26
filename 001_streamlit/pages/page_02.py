# streamlit run  "C:\Users\ikega\OneDrive\デスクトップ\001_streamlit_0test\pages\page_01.py"

import streamlit as st
from PIL import Image

import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader


# 変数Localの値を選択
    # 1＜ローカル＞または2＜クラウド＞を選べるようにする
Local = 2
# Localの値によって異なるパスを指定
if Local == 1:
    ## ユーザー設定読み込み
    yaml_path = r"C:\Users\ikega\OneDrive\デスクトップ\001_streamlit_0test\confug.yaml"
elif Local == 2:
    ## ユーザー設定読み込み
    yaml_path = "001_streamlit_0test/confug.yaml"


with open(yaml_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie_name=config['cookie']['name'],
    cookie_key=config['cookie']['key'],
    cookie_expiry_days=config['cookie']['expiry_days'],
)

## UI 
authenticator.login()
if st.session_state["authentication_status"]:
    ## ログイン成功
    with st.sidebar:
        st.markdown(f'## Welcome *{st.session_state["name"]}*')
        authenticator.logout('Logout', 'sidebar')
        st.divider()
    #st.write('# ログインしました!')
    st.markdown(
        "<h12 style='color: blue;'>【ログイン済み】</h12>",
        unsafe_allow_html=True
    )
    st.title('ページ2')

    # Localの値によって異なるパスを指定
    if Local == 1:
    ## ユーザー設定読み込み
        poto = Image.open(r"C:\Users\ikega\OneDrive\デスクトップ\001_streamlit_0test\data\k02.jpg")
        st.image(poto,width=50)
    elif Local == 2:
    ## ユーザー設定読み込み
        poto = Image.open("001_streamlit_0test\data\k02.jpg")
        st.image(poto,width=50)


elif st.session_state["authentication_status"] is False:
    ## ログイン成功ログイン失敗
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    ## デフォルト
    st.warning('Please enter your username and password')






