import streamlit as st
from PIL import Image

st.title("ぎょうざのホームページ")
st.caption("streamlitで開発するホームページアプリ")

image = Image.open('./data/yadon_koiking.jpg')
st.image(image, width=200)
