# 건의사항 탭

import streamlit as st
import sqlite3
import time
import pandas as pd

conn = sqlite3.connect('suggestion1.db', check_same_thread=False)
cur = conn.cursor()

def create_tb():
    cur.execute('CREATE TABLE IF NOT EXISTS suggestion1(author CHAR, email VARCHAR, title TEXT, comment MEDIUMTEXT, date TEXT)' )
    conn.commit()

# 데이터 쓰기
def add_data(author, email, title, date, comment):
    params = (author, email, title, str(date), comment)
    cur.execute("INSERT INTO suggestion1(author, email, title, date, comment) VALUES (?,?,?,?,?)",params)
    conn.commit()

# 목록
def sugg_list():
    try:
        cur.execute('SELECT author, title, date, comment FROM suggestion1')
        sugg = cur.fetchall()
        return sugg
    except:
        return

# # 수정 (update)
# def data_update(username):
#     pass
# # 삭제 (delete)
# def data_delete(username):
#     cur.execute('DELETE FROM suggestion WHERE AUTHOR =:AUTHOR' ,{'AUTHOR':author})
#     conn.commit()
#     # conn.close()

def run_suggestions():
    st.subheader("""
    건의사항💢
    - *궁금하시거나 불편하신 점 있으시면 게시판 등록해주세요!*
    """)

    # 문의사항 입력
    with st.expander("문의하기"):
        form = st.form(key="annotation")
        with form:
            create_tb()
            cols = st.columns((1,1))
            author = cols[0].text_input("작성자명 ", max_chars = 4)
            email = cols[1].text_input("이메일 ")
            title = st.text_input("제목", max_chars = 30)
            comment = st.text_area("내용 ")
            submit = st.form_submit_button(label="작성")
            date = time.strftime('%Y.%m.%d %H:%M')
            if submit:
                add_data(author, email, title, comment, date)
                st.success("문의하신 내용이 접수되었습니다!")
                st.balloons()
    container = st.container()
    with container:
        list = sugg_list()
        # st.write(list)
        df = pd.DataFrame(list, columns=['작성자명', '제목', '내용', '작성시각'])
        st.dataframe(df)