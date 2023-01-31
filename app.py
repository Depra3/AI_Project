# -*- coding : utf-8 -*-

import streamlit as st

def main():
    
    # 타이틀 
    st.title("실거래기반 서울 월세 추천 매물")

    # 사이드 바
    menu = ['Home', '월세 검색', '실거래 매물', '게시판']
    choice = st.sidebar.selectbox('메뉴', menu)

    # table()
    st.subheader("추천매물")
    # 인기 매물 보여주기
    st.table()


if __name__ == "__main__":
    main()