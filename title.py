# 홈 탭

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import math
import plotly.graph_objects as go
import plotly.express as px
# import tensorflow as tf
# import yfinance as yf
import requests

# print("tensorflow", str(tf.__version__))
# print("yfinance", str(tf.__version__))

def run_title():
    """홈페이지에서 인덱스화면을 표시하는 함수입니다.
    Args:
        

    Returns:
        

    Raises:
        ValueError : 
    """
    # 서울시공공데이터에서 인증키를 받아 데이터를 받아옴
    # https://data.seoul.go.kr/dataList/OA-21276/S/1/datasetView.do
    # 인증키 : 
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    st.markdown("""
    ## 👑실거래 현황
    - *현재까지의 서울시 집에 대한 실거래가 현황입니다!*
    - 기간 : 2022.01.01~ 2023.01.30 (계약일 기준)
    """)
    data_copy = data.copy()
    data_copy['FLR_NO'] = data_copy['FLR_NO'].astype(str) + '층'
    cols = ['BOBN', 'BUBN']
    data_copy['번지'] = data_copy[cols].apply(lambda row: '-'.join(row.values.astype(str))
                                            if row['BUBN'] != 0
                                            else row['BOBN'], axis=1)
    data_copy['BLDG_NM'] = data_copy['BLDG_NM'].str.replace('아파트', '')
    data_copy['BLDG_NM'] = data_copy['BLDG_NM'].str.replace('오피스텔', '')                             
    cols1 = ['SGG_NM', 'BJDONG_NM', '번지', 'BLDG_NM', 'HOUSE_GBN_NM', 'FLR_NO']
    data_copy['주소'] = data_copy[cols1].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
    data_copy = data_copy.drop(['SGG_CD', 'BJDONG_CD', 'SGG_NM', 'BJDONG_NM', 'BOBN', 'BUBN', 'FLR_NO', 'BLDG_NM', '번지', 'HOUSE_GBN_NM'], axis=1)
    data_copy['RENT_AREA'] = data_copy['RENT_AREA'].apply(lambda x: math.trunc(x / 3.3058))
    data_copy.columns = ['계약일', '전월세 구분', '임대면적(평)', '보증금(만원)', '임대료(만원)', '건축년도', '주소']
    data_copy = data_copy[['계약일', '주소', '보증금(만원)', '임대료(만원)', '임대면적(평)', '건축년도', '전월세 구분']]
    data_copy = data_copy.reset_index(drop=True)
    data_copy.index = data_copy.index+1
    st.write(data_copy)

    t1, t2 = st.tabs(['전세 월평균 그래프', '월세 월평균 그래프'])
    j_m_mean = pd.read_csv('data/gu_j_m_mean.csv', encoding='cp949')
    w_m_mean = pd.read_csv('data/gu_w_m_mean.csv', encoding='cp949')

    gu = np.array(j_m_mean['SGG_NM'].unique())

    with t1:
        c1 = st.checkbox('전세 월평균 그래프', True)
        
        fig = go.Figure()
        dic = {}
        if c1:
            fig = px.scatter(width=700)
            for i in gu:
                dic.update({i : j_m_mean[j_m_mean['SGG_NM']==i]['RENT_GTN']})
            
            for j in gu:
                df = j_m_mean[j_m_mean['SGG_NM']==j]
                fig.add_scatter(x=df['YM'], y=df['RENT_GTN'], name=j)
            fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')
            st.plotly_chart(fig)

        else:
            st.write(j_m_mean)

    with t2:
        c1, c2 = st.columns([1,1])
        s1 = c1.checkbox('보증금 월평균 그래프', True)
        s2 = c2.checkbox('월세 월평균 그래프', True)

        p1 = c1.empty()
        p2 = c2.empty()
        
        fig = go.Figure()
        dic = {}
        if s1:
            with p1.container():
                fig = px.scatter(width=350)
                for i in gu:
                    dic.update({i : w_m_mean[w_m_mean['SGG_NM']==i]['RENT_GTN']})
                
                for j in gu:
                    df = w_m_mean[w_m_mean['SGG_NM']==j]
                    fig.add_scatter(x=df['YM'], y=df['RENT_GTN'], name=j)
                fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(k=천만원)')
                st.plotly_chart(fig)

        else:
            c1.write(j_m_mean)
            p1 = st.empty()

        if s2:
            with p2.container():
                fig = px.scatter(width=350)
                for i in gu:
                    dic.update({i : w_m_mean[w_m_mean['SGG_NM']==i]['RENT_GTN']})
                
                for j in gu:
                    df = w_m_mean[w_m_mean['SGG_NM']==j]
                    
                    fig.add_scatter(x=df['YM'], y=df['RENT_FEE'], name=j)
                fig.update_layout(xaxis_title='날짜', yaxis_title='보증금(만원)')
                st.plotly_chart(fig)
        else:
            c2.write(w_m_mean)
            p2 = st.empty()
    
    # 실거래 수 지역 순위
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("""
        💵월세 실거래수 지역 순위
        - *현재 월세 실거래수 TOP 10*🥇
        """)
        # 월세인 데이터 추출
        data_m = data[data['RENT_GBN'] == '월세']
        # 구, 동 합치기
        cols = ['SGG_NM', 'BJDONG_NM']
        data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
        data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
        #인덱스 재지정
        data_addr = data_addr.reset_index(drop=True)
        data_addr.index = data_addr.index+1

        # 그래프
        c1 = st.checkbox('월세 실거래 수 지역 순위 그래프', True)
        fig = go.Figure()
        if c1:
            fig = px.bar(x=data_addr.head(10)['주소'], y=data_addr.head(10)['거래 수'], width=350,
                        color=data_addr.head(10)['주소'])
            fig.update_layout(xaxis_title='지역 동', yaxis_title='보증금(만원)')
            st.plotly_chart(fig)
        else:
            # 데이터
            st.write(data_addr.head(10))

    # 전세 실거래 수 지역 순위(월세와 같은 방식)
    with col2:
        st.subheader("""
        💳전세 실거래수 지역 순위
        - *현재 전세 실거래수 TOP10*🏆
        """)
        data_m = data[data['RENT_GBN']=='전세']
        cols = ['SGG_NM', 'BJDONG_NM']
        data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
        data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
        data_addr = data_addr.reset_index(drop=True)
        data_addr.index = data_addr.index+1
        # 그래프
        c1 = st.checkbox('전세 실거래 수 지역 순위 그래프', True)
        fig = go.Figure()
        if c1:
            fig = px.bar(x=data_addr.head(10)['주소'], y=data_addr.head(10)['거래 수'], width=350,
                        color=data_addr.head(10)['주소'])
            fig.update_layout(xaxis_title='지역 동', yaxis_title='보증금(만원)')
            st.plotly_chart(fig)
        else:
            # 데이터
            st.write(data_addr.head(10))




        
    #     # st.write()보여주기
    #     st.write(data_addr.head(10))
    # with col2:
    #     st.subheader("""
    #     💳전세 실거래수 지역 순위
    #     - *현재 전세 실거래수 TOP10*🏆
    #     """)
    #     # 전세인 데이터 추출
    #     data_m = data[data['RENT_GBN']=='전세']
    #     # 구, 동 합치기
    #     cols = ['SGG_NM', 'BJDONG_NM']
    #     data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
    #     data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
    #     # 인덱스 재지정
    #     data_addr = data_addr.reset_index(drop=True)
    #     data_addr.index = data_addr.index+1
        
    #     # st.write()보여주기
    #     st.write(data_addr.head(10))
