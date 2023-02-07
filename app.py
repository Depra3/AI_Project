# -*- coding : utf-8 -*-

import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import requests

import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 다른 파일의 함수를 불러온다
from title import run_title
from search import run_search
from predict import run_predict
from suggestions import run_suggestions


st.title('🏘️내 방, 어디👀?')


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
# data = pd.read_csv('data/bds_data.csv', encoding='cp949')

# for j in range(1,2):
#     service_key = '4d42486779706d3034365957634870'
#     # url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/{1+((j-1)*1000)}/{j*1000}'
#     url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/\
#         tbLnOpendataRentV/{1+((j-1)*1000)}/{j*1000}/ / / / / / / /20230131'
#     print(url)
#     req = requests.get(url)
#     content_1 = req.text
    # content = req.json()
    # con = content['tbLnOpendataRentV']['row']

#     for h in con:
#         dic = {}
#         dic['SGG_CD'] = h['SGG_CD']
#         dic['SGG_NM'] = h['SGG_NM']
#         dic['BJDONG_CD'] = h['BJDONG_CD']
#         dic['BJDONG_NM'] = h['BJDONG_NM']
#         dic['BOBN'] = h['BOBN']
#         dic['BUBN'] = h['BUBN']
#         dic['FLR_NO'] = h['FLR_NO']
#         dic['CNTRCT_DE'] = h['CNTRCT_DE']
#         dic['RENT_GBN'] = h['RENT_GBN']
#         dic['RENT_AREA'] = h['RENT_AREA']
#         dic['RENT_GTN'] = h['RENT_GTN']
#         dic['RENT_FEE'] = h['RENT_FEE']
#         dic['BLDG_NM'] = h['BLDG_NM']
#         dic['BUILD_YEAR'] = h['BUILD_YEAR']
#         dic['HOUSE_GBN_NM'] = h['HOUSE_GBN_NM']
#         data.append(dic)
# #   ===
# # --
# df = pd.DataFrame(data)
# df['BOBN'].replace('', np.nan, inplace=True)
# df['BUBN'].replace('', np.nan, inplace=True)
# df['BLDG_NM'].replace('', np.nan, inplace=True)
# df['BUILD_YEAR'].replace('', np.nan, inplace=True)
# df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
# df['CNTRCT_DE'] = df['CNTRCT_DE'].apply(lambda x: pd.to_datetime(str(x), format="%Y/%m/%d"))
# df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
# df['CNTRCT_DE'].replace('T00:00:00', '', inplace=True)
# df = df.dropna()
# st.write(df['CNTRCT_DE'] == '20230131')


#######################################################################
#######################################################################
#######################################################################

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