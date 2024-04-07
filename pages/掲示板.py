import streamlit as st
import sqlite3
import datetime
import pytz

st.title("ぎょうざのホームページ")
st.caption("streamlitでホームページ作ってみた")
st.subheader('簡易的な掲示板です')


dbname = 'POSTS.db'
con = sqlite3.connect(dbname)

#sqliteを操作するカーソルを作成
cur = con.cursor()

#postsというtableを作成する
cur.execute('''
    CREATE TABLE IF NOT EXISTS posts(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      body TEXT,
      date TEXT   
      )''')

con.commit()
cur.close()
con.close()

with st.form(key="post_form"):
    #入力フォーム
    name = st.text_input("名前")
    body = st.text_area('文章を入力してください',height=200)
    #送信ボタン
    submit_btn = st.form_submit_button("送信")
    if submit_btn:
        con = sqlite3.connect(dbname)
        cur = con.cursor()
        #dbにデータを入れる
        cur.execute(f'''
            INSERT INTO posts
            (name,body,date)
            VALUES
            ('{name}','{body}','{datetime.datetime.now(pytz.timezone("Asia/Tokyo"))}')
            ''')
        con.commit()
        con.close()
        
con = sqlite3.connect(dbname)
cur = con.cursor()
db_posts = cur.execute("SELECT * FROM posts").fetchall()
cur.close()
con.close()
posts = []
for row in db_posts:
    posts.append({"id":row[0], "name":row[1], "body":row[2], "date":row[3]})

for post in posts:
    with st.container():
        st.write(post["id"],post["name"],post["date"])
        st.text(post["body"])

