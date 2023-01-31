# -*- coding : utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# 다른 파일의 함수를 불러온다
from run_title2 import run_title2

# data = pd.read_csv('data/dbs_data.csv')

# def main():
#     title()
    
    # 타이틀 
    # st.title("실거래기반 서울 월세 추천 매물")

    # 사이드 바
    # menu = ['홈', '월세 검색', '실거래 매물', '게시판']
    # choice = st.sidebar.selectbox('메뉴', menu)

    # if choice == '홈':
    #     st.subheader("홈")
    #     st.markdown(dec_temp, unsafe_allow_html=True)
    # if choice == '홈':
    #     st.title("실거래기반 서울 월세 추천 매물")
    #     # table()
    #     st.subheader("홈")
    #     # 인기 매물 보여주기
    #     # data = pd.read_csv('data/dbs_data.csv')
    #     st.table()
    #     # sepal_length = st.sidebar.select_slider('월세', options = np.arange(0, 5000))
    # elif choice == '월세 검색':
    #     st.subheader("월세 검색")


    # elif choice == '실거래 매물':
    #     st.subheader("실거래 매물")
        
    # else:
    #     st.subheader("게시판")



    # # table()
    # st.subheader("추천매물")
    # # 인기 매물 보여주기
    # st.table()


def main():
    # st.title('TITLE')

    selected3 = option_menu(None, ["🏠Home", " 🔎전월세 검색",  "📊전세vs월세?", '💬건의사항'], 
        # icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "gray", "font-size": "15px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#47C83E"},
        }
    )
    data = pd.read_csv('data/bds_data_1.csv', encoding='cp949')

    if selected3 == "🏠Home":
        st.title('TITLE')
        # data = pd.read_csv('data/bds_data_1.csv', encoding='cp949')
        st.write(data.head())

    elif selected3 == " 🔎전월세 검색":
        # st.sidebar.selectbox('menu', [1,2,3,4,5]) 
        run_title2()

    elif selected3 == " 📊전세vs월세?":
        pass
    else:
        pass







if __name__ == "__main__":
    main()