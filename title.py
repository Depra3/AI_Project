# 홈 탭

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd


def run_title():
    # 서울시공공데이터에서 인증키를 받아 데이터를 받아옴
    # https://data.seoul.go.kr/dataList/OA-21276/S/1/datasetView.do
    # 인증키 : 4d42486779706d3034365957634870
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    st.markdown("""
    ## 👑실거래 현황
    - *현재까지의 서울시 집에 대한 실거래가 현황입니다!*
    """)
    data_copy = data.copy()
    data_copy.columns = ['구코드', '구이름', '동코드', '동이름', '번지', '번지_', 
    '층수', '계약일', '전세/월세', '임대면적', '보증금', '임대료', 
    '건물이름', '건축년도', '건물타입']
    # data.columns = ['구코드', '구이름', '동코드', '동이름', '번지', '번지_', 
    # '층수', '계약일', '전세/월세', '임대면적', '보증금', '임대료', 
    # '건물이름', '건축년도', '건물타입']
    st.write(data_copy)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("""
        💵월세 실거래수 지역 순위
        - *현재 월세 실거래수 TOP 10*
        """)
        data_m = data[data['RENT_GBN']=='월세']
        cols = ['SGG_NM', 'BJDONG_NM']
        data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
        data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
        data_addr = data_addr.reset_index(drop=True)
        data_addr.index = data_addr.index+1
        st.write(data_addr.head(10))
    with col2:
        st.subheader("""
        💳전세 실거래수 지역 순위
        - *현재 전세 실거래수 TOP10*
        """)
        data_m = data[data['RENT_GBN']=='전세']
        cols = ['SGG_NM', 'BJDONG_NM']
        data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
        data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
        data_addr = data_addr.reset_index(drop=True)
        data_addr.index = data_addr.index+1
        st.write(data_addr.head(10))

    # st.title('TITLE')

    # selected3 = option_menu(None, ["🏠Home", " 🔎전월세 검색",  "📊전세vs월세?", '💬건의사항'], 
    #     # icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #     menu_icon="cast", default_index=0, orientation="horizontal",
    #     styles={
    #         "container": {"padding": "0!important", "background-color": "#fafafa"},
    #         "icon": {"color": "gray", "font-size": "15px"}, 
    #         "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
    #         "nav-link-selected": {"background-color": "#47C83E"},
    #     }
    # )