import streamlit as st

st.title("ぎょうざのホームページ")
st.caption("streamlitでホームページ作ってみた")
st.subheader('文章を入力して送信すれば文字数を数えてくれます')

with st.form(key='str_counting'):  
    text_input = st.text_area('文章を入力してください',height=500,)
    submit_btn = st.form_submit_button("送信")
    if submit_btn:
        st.text(f'{len(text_input)}文字')
