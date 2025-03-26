# streamlit run  "C:\Users\ikega\OneDrive\デスクトップ\001_streamlit_0test\pages\page_01.py"

import os
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from PIL import Image
from yaml.loader import SafeLoader

# 相対パスの生成
# 現在のファイルのディレクトリを取得
current_dir1 = os.path.dirname(__file__)

# 上記のディレクトリの親ディレクトリを取得
current_dir2 = os.path.dirname(current_dir1)

# 親ディレクトリを取得から作りたいパスを作成
yaml_path = os.path.join(current_dir2, 'config.yaml')

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

    # 親ディレクトリを取得から作りたいパスを作成
    poto2 = os.path.join(current_dir2, 'data', 'k02.jpg')

    # Streamlitで画像を表示
    st.image(poto2, width=100, caption="カレントディレクトリから絶体パスを作成")

elif st.session_state["authentication_status"] is False:
    ## ログイン成功ログイン失敗
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    ## デフォルト
    st.warning('Please enter your username and password')






