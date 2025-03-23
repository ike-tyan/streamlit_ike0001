import streamlit as st
from PIL import Image


#画面を左右に分解
left1_column, right1_column = st.columns(2)

#左側
#イメージ画像
photo = Image.open('レシート_001.jpg')
left1_column.image(photo, caption='レシート類')

#右側
#タイトル
right1_column.title("仕訳確認S")
right1_column.write("AI-OCRの結果を現物を見て確認&訂正")

#テキストボックス(単純)
kamoku = right1_column.text_input('科目','消耗品費')
yy = right1_column.text_input('令和','7')
mmdd= right1_column.text_input('月日(0101)','1231')

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
t_banngou = right1_column.text_input('登録番号','T1234567890123')
tekiyou1 = right1_column.text_input('摘要1','セブンイレブン静岡森下町店')
tekiyou1 = right1_column.text_input('摘要2','来客用缶コーヒー')



#ボタンを横に並べる
left_column, right_column = st.columns(2)
left_column.button('ボタン左')
right_column.button('ボタン右')

#ボタン
#choose_btn = st.button('選択')
#clear_btn = st.button('クリア')

