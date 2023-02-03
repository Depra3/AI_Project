# 건의사항 탭

import streamlit as st
import sqlite3
import time
import pandas as pd

conn = sqlite3.connect('suggestion.db', check_same_thread=False)
cur = conn.cursor()

# 테이블 생성
def create_tb():
    cur.execute('CREATE TABLE IF NOT EXISTS suggestion(author CHAR, email VARCHAR, title TEXT, comment TEXT, date TEXT, status TEXT)' )
    conn.commit()

# db 입력
def add_data(author, email, title, date, comment, status):
    params = (author, email, title, str(date), comment, status)
    cur.execute("INSERT INTO suggestion(author, email, title, date, comment, status) VALUES (?,?,?,?,?,?)",params)
    conn.commit()

# 목록 불러오기
def sugg_list():
    cur.execute('SELECT author, title, date, comment, status FROM suggestion')
    sugg = cur.fetchall()
    return sugg

# 검색 (작성자명)
def get_by_author(author):
	cur.execute("SELECT author, title, date, comment, status FROM suggestion WHERE author like '%{}%'".format(author))
	data = cur.fetchall()
	return data
# 검색(제목)
def get_by_title(title):
	cur.execute("SELECT author, title, date, comment, status FROM suggestion WHERE title like '%{}%'".format(title))
	data = cur.fetchall()
	return data
# 검색(내용)
def get_by_comment(comment):
	cur.execute("SELECT author, title, date, comment, status FROM suggestion WHERE date like '%{}%'".format(comment))
	data = cur.fetchall()
	return data

# 처리상태 수정
def update_status(email):
    cur.execute('UPDATE suggestion SET status = "처리완료" WHERE email="{}"'.format(email))
    conn.commit()
def recover_status(email):
    cur.execute('UPDATE suggestion SET status = "접수" WHERE email="{}"'.format(email))
    conn.commit()

def delete_post(email):
    cur.execute('DELETE FROM suggestion WHERE email = "{}"'.format(email))
    conn.commit()
     # conn.close()


# ▲ DB 관련
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

def run_suggestions():
    st.subheader('건의사항')

    # 문의사항 입력
    with st.expander("문의하기"):
        form = st.form(key="annotation")
        with form:
            create_tb()
            cols = st.columns((1,1))
            author = cols[0].text_input("작성자명 ", max_chars = 12)
            email = cols[1].text_input("이메일 ")
            title = st.text_input("제목", max_chars = 50)
            comment = st.text_area("내용 ")
            submit = st.form_submit_button(label="작성")
            date = time.strftime('%Y.%m.%d %H:%M:%S')
            status = "접수"
            if submit:
                # 문의사항 접수
                if submit:
                    if author == "" or email == "" or title == "" or comment == "":
                        st.error('빈칸을 확인해주세요.')
                else:
                    add_data(author, email, title, comment, date, status)
                    st.success("문의하신 내용이 접수되었습니다! 답변은 작성해주신 이메일로 발송됩니다. 감사합니다.")
                # add_data(author, email, title, comment, date, status)
                # st.success("문의하신 내용이 접수되었습니다! 답변은 이메일로 발송됩니다. 감사합니다.")
                    st.snow()

    # 검색
    with st.expander("검색"):
        cols = st.columns((1,1))
        search_term = cols[0].text_input(' ')
        search_option = cols[1].selectbox(" ",("--검색옵션--","내용","작성자명","제목"))
        if st.button("검색"):
                if search_term == "":
                    st.warning("검색어를 입력하세요")
                elif search_option == "내용":
                    result=get_by_comment(search_term)
                    s_result = pd.DataFrame(result, columns=['작성자명', '제목', '내용', '작성시각', '상태'])
                    st.dataframe(s_result, use_container_width=True)
                elif search_option =="작성자명":
                    result=get_by_author(search_term)
                    s_result = pd.DataFrame(result, columns=['작성자명', '제목', '내용', '작성시각', '상태'])
                    st.dataframe(s_result, use_container_width=True)
                elif search_option =="제목":
                    result=get_by_title(search_term)
                    s_result = pd.DataFrame(result, columns=['작성자명', '제목', '내용', '작성시각', '상태'])
                    st.dataframe(s_result, use_container_width=True)
                else :
                    st.warning("검색옵션을 입력하세요")


    # 목록
    container = st.container()
    with container:
        list = sugg_list()
        # st.write(list)
        df = pd.DataFrame(list, columns=['작성자명', '제목', '내용', '작성시각', '상태'])
        # st.dataframe(df.style.set_properties(subset=['내용'], **{'width': '1000px'}))
        st.dataframe(df, use_container_width=True)
        # st.table(df)


    # 관리자 기능
    admin_option = st.checkbox("관리자 메뉴")
    if admin_option:
        cols = st.columns((1,1))
        command = cols[0].text_input("command")
        email = cols[1].text_input("email")
        if st.button ("확인"):
            if command == "ok_myroomadmin":
                update_status(email)
            elif command == "no_myroomadmin":
                recover_status(email)
            elif command == "del_myroomadmin":
                st.checkbox("삭제하시겠습니까? 작성하신 이메일을 다시 확인해주세요.")
                # del_reason = st.text_input("삭제사유")
                delete_post(email)
            else :
                st.warning("잘못된 명령입니다")


# conn = sqlite3.connect('suggestion.db', check_same_thread=False)
# cur = conn.cursor()

# # conn_1 = sqlite3.connect("text.db")
# # cur_1 = conn_1.cursor()
# # test_t = "('CREATE TABLE IF NOT EXISTS test(author CHAR not null, email VARCHAR not null, title TEXT not null, comment MEDIUMTEXT not null, date TEXT not null, status TEXT not null)' )"
# # cur_1.execute(test_t)
# # conn.commit()

# # 테이블 생성
# def create_tb():
#     # cur.execute('CREATE TABLE IF NOT EXISTS suggestion(author CHAR, email VARCHAR, title TEXT, comment MEDIUMTEXT, date TEXT, status TEXT)')
#     cur.execute('CREATE TABLE IF NOT EXISTS suggestion1111(author CHAR, email VARCHAR, title TEXT, comment TEXT, date TEXT, status TEXT)')
    
#     conn.commit()

# # db 입력
# # def add_data(author, email, title, date, comment, status):
# #     params = (author, email, title, str(date), comment, status)
# #     cur.execute("INSERT INTO suggestion11(author, email, title, date, comment, status) VALUES (?,?,?,?,?,?)",params)
# #     conn.commit()
# def add_data(author, email, title, comment, date, status):
#     params = (author, email, title, comment, str(date), status)
#     cur.execute("INSERT INTO suggestion1111(author, email, title, comment, date, status) VALUES (?,?,?,?,?,?)",params)
#     conn.commit()

# # 목록 불러오기
# def sugg_list():
#     cur.execute('SELECT author, title, comment, date, status FROM suggestion1111')
#     sugg = cur.fetchall()
#     return sugg

# # # 수정 (update)
# # def data_update(username):
# #     pass
# # # 삭제 (delete)
# # def data_delete(username):
# #     cur.execute('DELETE FROM suggestion WHERE AUTHOR =:AUTHOR' ,{'AUTHOR':author})
# #     conn.commit()
# #     # conn.close()

# # 검색 (작성자명)
# def get_by_author(author):
# 	cur.execute("SELECT author, title, coment, date, status FROM suggestion1111 WHERE author like '%{}%'".format(author))
# 	data = cur.fetchall()
# 	return data
# # 검색(제목)
# def get_by_title(title):
# 	cur.execute("SELECT author, title, comment, date, status FROM suggestion111 WHERE title like '%{}%'".format(title))
# 	data = cur.fetchall()
# 	return data
# # 검색(내용)
# def get_by_comment(comment):
# 	cur.execute("SELECT author, title, comment, comment, status FROM suggestion111 WHERE commet like '%{}%'".format(comment))
# 	data = cur.fetchall()
# 	return data

# # 처리상태 수정
# def update_status(email):
#     cur.execute('UPDATE suggestion111 SET status = "처리완료" WHERE email="{}"'.format(email))
#     conn.commit()
# def recover_status(email):
#     cur.execute('UPDATE suggestion111 SET status = "접수" WHERE email="{}"'.format(email))
#     conn.commit()


# # ▲ DB 관련
# # -------------------------------------------------------------------------------------------------
# # -------------------------------------------------------------------------------------------------
# # -------------------------------------------------------------------------------------------------

# def run_suggestions():
#     st.subheader("""
#     건의사항💢
#     - *궁금하시거나 불편하신 점 있으시면 게시판 등록해주세요!!*
#     """)

#     # 문의사항 입력
#     with st.expander("문의하기"):
#         form = st.form(key="annotation")
#         with form:
#             create_tb()
#             cols = st.columns((1,1))
#             author = cols[0].text_input("작성자명 ", max_chars = 12)
#             email = cols[1].text_input("이메일 ")
#             title = st.text_input("제목", max_chars = 50)
#             comment = st.text_area("내용 ")
#             submit_cols = st.columns((1,1))
#             submit = submit_cols[0].form_submit_button(label="작성")
#             submit_1 = submit_cols[1].form_submit_button(label="수정")   
#             date = time.strftime('%Y.%m.%d %H:%M')
#             status = "접수"
#             if submit:
#                 if author == "" or email == "" or title == "" or comment == "":
#                     st.error('빈칸을 확인하세요')
#                 else:
#                     add_data(author, email, title, comment, date, status)
#                     st.success("문의하신 내용이 접수되었습니다! 답변은 작성해주신 이메일로 발송됩니다. 감사합니다.")
#             if submit_1:
#                 # 내용란에 아래 글 입력, 이메일에 처리된 이메일 입력시 "처리완료" 혹은 "접수"로 변경함
#                 if comment == "ok_myroomadmin":
#                     update_status(email)

#                 elif comment == "no_myroomadmin":
#                     recover_status(email)
#                 else:
#                      st.error("관리자 권한입니다!!")
#             #     else :
#             #         add_data(author, email, title, comment, date, status)
#             #         st.success("문의하신 내용이 접수되었습니다! 답변은 작성해주신 이메일로 발송됩니다. 감사합니다.")
#             #         st.balloons()

#     # 검색
#     with st.expander("검색"):
#         cols = st.columns((1,1,1))
#         search_term = cols[0].text_input('검색')
#         search_option = cols[1].selectbox("검색옵션",("내용","작성자명","제목"))
#         if cols[2].button("검색"):
#                 if search_option == "내용":
#                     result = get_by_comment(search_term)

#                 elif search_option == "작성자명":
#                     # result = get_by_author(search_term)
                    
#                     if search_term == "":
#                         st.error(" '빈칸을 확인해주세요.' ")
#                         result = pd.DataFrame(columns=['작성자명', '제목', '내용', '작성시각', '상태'])
#                     else:
#                         result = get_by_author(search_term)
#                 elif search_option == "제목":
#                     if search_term == "":
#                         st.error(" '빈칸을 확인해주세요.' ")
#                         result = pd.DataFrame(columns=['작성자명', '제목', '내용', '작성시각', '상태'])
#                     else:
#                         result = get_by_title(search_term)
#                     # result=get_by_title(search_term)
#                     # if search_term == "":
#                     #     st.error("빈칸을 확인해주세요.")

#                 s_result = pd.DataFrame(result, columns=['작성자명', '제목', '내용', '작성시각', '상태'])
#                 st.dataframe(s_result, use_container_width=True)

#                 # cur.execute("select date from suggestion11")
#                 # a = cur.fetchall()
#                 # st.write(a)



#     # 목록
#     container = st.container()
#     with container:
#         list = sugg_list()
#         # st.write(list)
#         df = pd.DataFrame(list, columns=['작성자명', '제목', '내용', '작성시각', '상태'])
#         # st.dataframe(df.style.set_properties(subset=['내용'], **{'width': '1000px'}))
#         st.dataframe(df, use_container_width=True)
#         # st.table(df)

# ======================================================

# conn = sqlite3.connect('suggestion1.db', check_same_thread=False)
# cur = conn.cursor()

# def create_tb():
#     cur.execute('CREATE TABLE IF NOT EXISTS suggestion1(author CHAR, email VARCHAR, title TEXT, comment MEDIUMTEXT, date TEXT)' )
#     conn.commit()

# # 데이터 쓰기
# def add_data(author, email, title, date, comment):
#     params = (author, email, title, str(date), comment)
#     cur.execute("INSERT INTO suggestion1(author, email, title, date, comment) VALUES (?,?,?,?,?)",params)
#     conn.commit()

# # 목록
# def sugg_list():
#     try:
#         cur.execute('SELECT author, title, date, comment FROM suggestion1')
#         sugg = cur.fetchall()
#         return sugg
#     except:
#         return

# # # 수정 (update)
# # def data_update(username):
# #     pass
# # # 삭제 (delete)
# # def data_delete(username):
# #     cur.execute('DELETE FROM suggestion WHERE AUTHOR =:AUTHOR' ,{'AUTHOR':author})
# #     conn.commit()
# #     # conn.close()

# def run_suggestions():
#     st.subheader("""
#     ## 건의사항💢
#     - *궁금하시거나 불편하신 점 있으시면 게시판 등록해주세요!!*
#     """)

#     # 문의사항 입력
#     with st.expander("문의하기"):
#         form = st.form(key="annotation")
#         with form:
#             create_tb()
#             cols = st.columns((1,1))
#             author = cols[0].text_input("작성자명 ", max_chars = 4)
#             email = cols[1].text_input("이메일 ")
#             title = st.text_input("제목", max_chars = 30)
#             comment = st.text_area("내용 ")
#             submit = st.form_submit_button(label="작성")
#             date = time.strftime('%Y.%m.%d %H:%M')
#             if submit:
#                 add_data(author, email, title, comment, date)
#                 st.success("문의하신 내용이 접수되었습니다!")
#                 st.balloons()
#     container = st.container()
#     with container:
#         list = sugg_list()
#         # st.write(list)
#         df = pd.DataFrame(list, columns=['작성자명', '제목', '내용', '작성시각'])
#         st.dataframe(df)





