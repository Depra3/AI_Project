# -*- coding : utf-8 -*-

import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# 다른 파일의 함수를 불러온다
from title import run_title
from search import run_search
from predict import run_predict
from suggestions import run_suggestions


st.title('내 방, 어디?')

selected3 = option_menu(None, ["🏠Home", "🔎전월세 검색", "📊전세 예측?",
 '💬건의사항'], 
        # icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "gray", "font-size": "15px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#47C83E"},
    }
)

if selected3 == "🏠Home":
    # st.title('내 방, 어디?')
    # data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    # st.write(data.head())
    run_title()

elif selected3 == "🔎전월세 검색":
    run_search()

elif selected3 == "📊전세 예측?":
    run_predict()

elif selected3 == "💬건의사항":
    run_suggestions()

else:
    selected3 == "🏠Home"



# data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    # st.write(data)
    # data['BLDG_NM'].replace("오피스텔", "")
    # st.write(data)

# def main():

    # if selected3 == "🏠Home":
    #     st.title('내 방, 어디?')
    #     # data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    #     st.write(data.head())

    # elif selected3 == " 🔎전월세 검색":
    #     run_search()

    # elif selected3 == " 📊전세 예측?":
    #     run_predict()
    # elif selected3 == " 💬건의사항":
    #     run_suggestions()
    # else:
    #     selected3 == "🏠Home"




# if __name__ == "__main__":
#     main()