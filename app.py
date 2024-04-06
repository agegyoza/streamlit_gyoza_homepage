import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

#テキスト関連
st.title("ぎょうざのホームページ")
st.caption("streamlitで開発するホームページアプリ")

#画像
image = Image.open("yadon_koiking.jpg")
st.image(image, width=200)

col1, col2 = st.columns(2)

with col1:
    #テキスト
    st.subheader("自己紹介")
    st.text('pythonの勉強中、webアプリを作って公開したい\n'
            'と思ってます。まずはstreamlitで作ってみます。')

    code = """
    import streamlit as st

    st.title("ぎょうざのホームページ")
    """
    st.code(code, language="python")

    with st.form(key="profile_form"):
        #テキストボックス
        name = st.text_input("名前")
        address = st.text_input("住所")
        
        #ラジオボタン
        age_category = st.radio(
            "年齢層",
            ("子供(18才未満)", "大人(18才以上)"))
        
        #複数選択
        hobby = st.multiselect(
            "趣味",
            ("スポーツ","読書","プログラミング","アニメ・映画","釣り","料理")
        )

        #ボタン
        submit_btn = st.form_submit_button("送信")
        cancel_btn = st.form_submit_button("キャンセル")
        if submit_btn:
            st.text(f'ようこそ！{name}さん！{address}に書類を送りました！')
            st.text(f'年齢層: {age_category}')
            st.text(f'趣味: {", ".join(hobby)}')
            
with col2:
    #データ分析関連
    df = pd.read_csv('平均気温.csv', index_col='月')
    st.line_chart(df)
    st.bar_chart(df['2021年'])



