# streamlit run  "C:\Users\ikega\OneDrive\デスクトップ\001_streamlit_0test\pages\page_01.py"

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
current_dir2 = os.path.dirname(current_dir1)

## 【ログイン機能】ユーザー設定読み込み
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

## 【ログ作成機能】CSVファイルへの保存用関数
# 親ディレクトリを取得から作りたいパスを作成
login_history1 = os.path.join(current_dir2, 'login_history.csv')
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
        # 親ディレクトリを取得から作りたいパスを作成
        poto1 = os.path.join(current_dir2, 'data', 'k01.jpg')
        # Streamlitで画像を表示
        st.image(poto1, width=100, caption="パス：" + poto1)


    # 親ディレクトリを取得から作りたいパスを作成
    csv1 = os.path.join(current_dir2, 'data', 'data001.csv')
    #csvファイル読み込み
    df1 = pd.read_csv(csv1)

    #平均
    mean1 = df1.groupby('科目').mean(numeric_only=True)
    #最大値
    max1 = df1.groupby('科目').max(numeric_only=True)
    #最小値
    min1 = df1.groupby('科目').min(numeric_only=True)
    #合計
    sum1 = df1.groupby('科目').sum(numeric_only=True)
    #回数
    count1 = df1.groupby('科目').count()
    #表＜writeメソッド＞
    st.write(df1)
    st.write(sum1)
    

elif st.session_state["authentication_status"] is False:
    ## ログイン成功ログイン失敗
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    ## デフォルト
    st.warning('Please enter your username and password')
    





